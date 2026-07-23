# LG Home AI 팀 프로젝트

소프트웨어공학 팀 프로젝트 레포. LG Home AI 연구원 심사를 대상으로 하는 스마트홈 AI 서비스를 기획·구현한다.

> **심사는 기술을 본다.** 발표 스킬이나 문서 꾸밈이 아니라 "왜 이 문제에 AI가 필요한가", "실제로 무엇을 만들었는가", "데이터·구현이 현실적인가"가 평가 기준이다. 이 레포의 모든 문서·코드는 그 기준에 복무한다.

이 레포는 기존 Notion 워크스페이스를 GitHub로 이주한 결과물이다 (2026-07-21). Notion 원본 내용은 손대지 않고 그대로 옮겼고(`docs/process/`, `docs/ideas/`), 그 위에 GitHub 기반 협업 방법론을 새로 얹었다(`docs/methodology/`).

---

## 이 레포에 뭐가 있나

```
lg-home-ai-team/
├── README.md                          이 파일
├── CONTRIBUTING.md                    협업 규칙 — 처음 커밋하기 전에 읽기
├── docs/
│   ├── process/                       아이디어 설계 프로세스·선택 기준·회의록 (Notion 원본)
│   ├── ideas/                         Notion 이관 5건 + 이후 팀 제안
│   └── methodology/
│       ├── git-github-협업.md         git/GitHub 협업 가이드 (초보용)
│       └── toolchain.md               Notion→GitHub 저장층 셋업 가이드
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── idea.md                    아이디어 제안 이슈 템플릿
│   │   └── task.md                    작업 이슈 템플릿
│   ├── PULL_REQUEST_TEMPLATE.md       PR 템플릿
│   └── labels.md                      라벨 목록 (역할/상태/우선순위)
└── assets/                            이미지·다이어그램 원본 파일
```

### 어디서부터 볼까

- **처음 온 팀원**: `CONTRIBUTING.md` → `docs/methodology/git-github-협업.md` 순서로 읽는다.
- **아이디어 현황이 궁금하면**: `docs/process/아이디어-선택-기준.md`(판단 기준 + 4개 후보 비교)와 `docs/ideas/`(각 후보 상세) 를 본다.
- **왜 이런 프로세스로 아이디어를 짜는지 궁금하면**: `docs/process/아이디어-설계-프로세스.md` (9단계 설계 프레임워크, LG 역대 우수작 LOCUS/HomeQuest 분석 포함).
- **Notion → GitHub 이주가 왜/어떻게 됐는지 궁금하면**: `docs/process/_notion-recovery-index.md`.
- **툴 세팅(Obsidian, Dataview 등)이 필요하면**: `docs/methodology/toolchain.md`.

---

## 시작하는 법

```bash
git clone <이 레포 주소>
cd lg-home-ai-team
```

1. `CONTRIBUTING.md`를 읽고 브랜치/커밋/PR 규칙을 확인한다.
2. 새 작업은 항상 `main`에서 새 브랜치를 파서 시작한다 (`git switch -c feature/짧은-설명`).
3. 아이디어를 제안하고 싶으면 Issues → New Issue → "아이디어 제안" 템플릿을 쓴다.
4. 작업 단위를 쪼개고 싶으면 "작업(Task)" 템플릿으로 이슈를 연다.
5. 코드/문서 변경은 PR로 올리고, 팀원 1명 이상 리뷰를 받은 뒤 머지한다 (`main` 직접 push 금지).

자세한 절차와 왜 이 순서를 지키는지는 `docs/methodology/git-github-협업.md` § 5(순서와 노출 규범)를 참고한다.

---

## 팀

`docs/process/팀원-펜-컬러.md` 참고 (이의진 / 김예준 / 이서진).
