"""
CASAS 가구별 순서제약 마이닝 — H3(제약은 가구마다 다른가) 판별용.

owner: Joshua (개인 아이디어 검증)
input: CASAS labeled CSV (Zenodo 15708568, labeled_data.zip)
       기본 경로는 이 스크립트 옆의 casas/labeled/ 이고,
       CASAS_DIR 환경변수로 바꿀 수 있다.
run:   python3 mine_household_constraints.py

데이터 받기:
  curl -L -o labeled_data.zip \
    "https://zenodo.org/records/15708568/files/labeled_data.zip?download=1"
  unzip labeled_data.zip -d casas
non-effect: 이 스크립트는 인과나 해저드를 증명하지 않는다. 순서 규칙성만 센다.
"""
import csv, collections, os, re, itertools, sys

DATA = os.environ.get(
    'CASAS_DIR',
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'casas', 'labeled'),
)

def load_days(fn):
    days = collections.defaultdict(list)
    with open(fn) as f:
        for row in csv.reader(f):
            if len(row) < 5:
                continue
            m = re.match(r'(.+?)="begin"', row[4])
            if m:
                days[row[0]].append(m.group(1))
    return list(days.values())

def mine_precedence(sessions, acts, min_sup, conf_th):
    """Declare Precedence(A,B): B가 발생한 날엔 그 전에 A가 있었다."""
    found = {}
    for a, b in itertools.permutations(acts, 2):
        occ = sat = 0
        for s in sessions:
            if b not in s:
                continue
            occ += 1
            if a in s and s.index(a) < s.index(b):
                sat += 1
        if occ >= min_sup and sat / occ >= conf_th:
            found[(a, b)] = (sat, occ, sat / occ)
    return found

def run(n_house, top_acts, min_sup, conf_th, min_days=20, verbose=False):
    files = sorted(f for f in os.listdir(DATA) if f.endswith('.csv'))[:n_house]
    per = {}
    for fn in files:
        sess = load_days(os.path.join(DATA, fn))
        if len(sess) < min_days:
            continue
        cnt = collections.Counter(a for s in sess for a in s)
        acts = [a for a, _ in cnt.most_common(top_acts)]
        res = mine_precedence(sess, acts, min_sup, conf_th)
        per[fn] = set(res)
        if verbose:
            print(f"  {fn}: days={len(sess):4d} constraints={len(res)}")
    if not per:
        return None
    allc = set().union(*per.values())
    universal = set.intersection(*per.values())
    freq = collections.Counter(c for v in per.values() for c in v)
    solo = [c for c, n in freq.items() if n == 1]
    return dict(households=len(per), total=len(allc), universal=len(universal),
                solo=len(solo), solo_pct=100 * len(solo) / max(len(allc), 1),
                per_house=[len(v) for v in per.values()])

if __name__ == '__main__':
    if not os.path.isdir(DATA):
        sys.exit(
            f"CASAS 데이터를 찾을 수 없습니다: {DATA}\n"
            "docstring의 '데이터 받기'를 참고하거나 CASAS_DIR 환경변수를 설정하세요."
        )
    print("=== 견고성 검사: 임계값을 바꿔도 결론이 유지되는가 ===\n")
    print(f"{'가구':>4} {'활동':>4} {'최소지지':>8} {'신뢰도':>6} | {'제약종류':>8} {'보편':>5} {'고유':>5} {'고유%':>7}")
    for n_house in (20, 40):
        for top_acts in (10, 12, 15):
            for min_sup, conf in ((5, 0.95), (10, 0.90), (10, 0.99)):
                r = run(n_house, top_acts, min_sup, conf)
                if r:
                    print(f"{r['households']:>4} {top_acts:>4} {min_sup:>8} {conf:>6.2f} | "
                          f"{r['total']:>8} {r['universal']:>5} {r['solo']:>5} {r['solo_pct']:>6.1f}%")
