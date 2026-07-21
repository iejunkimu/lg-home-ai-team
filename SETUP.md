# GitHub 쪽 남은 설정

레포 자체(문서·템플릿·라벨 정의 파일)는 준비됐지만, GitHub 저장소 설정 화면에서 직접 눌러줘야 하는 항목들이 남아있다. 이 문서는 그 체크리스트다.

> ⚠️ **먼저 `gh auth login -h github.com` 재인증이 필요하다** (현재 로컬 `gh` 토큰이 만료/무효 상태). 아래 각 항목마다 (A) `gh` 명령 경로와 (B) 웹 UI 경로를 함께 적었다 — 재인증 전이면 (B) 웹 UI로 먼저 진행해도 된다.

```bash
gh auth login -h github.com
gh auth status   # 재인증 확인
```

---

## 1. 라벨 생성

`.github/labels.md`에 정의된 표를 실제 GitHub 라벨로 만든다.

### (A) `gh` 명령

```bash
# role
gh label create "role: ai" --color 1D76DB --description "AI·데이터 모델링 관련" --force
gh label create "role: backend" --color 1D76DB --description "백엔드·IoT 통신 관련" --force
gh label create "role: frontend" --color 1D76DB --description "프론트엔드·앱 UI 관련" --force
gh label create "role: docs" --color 1D76DB --description "문서·기획 관련" --force

# status
gh label create "status: 제안" --color 0E8A16 --description "새로 제안됨, 아직 논의 전" --force
gh label create "status: 토론중" --color FBCA04 --description "팀 논의가 진행 중" --force
gh label create "status: 채택" --color 0E8A16 --description "팀이 채택하기로 결정" --force
gh label create "status: 기각" --color B60205 --description "팀이 채택하지 않기로 결정" --force

# priority
gh label create "priority: high" --color D93F0B --description "이번 스프린트 내 처리 필요" --force
gh label create "priority: med" --color FBCA04 --description "가까운 시일 내 처리" --force
gh label create "priority: low" --color C2E0C6 --description "여유 있을 때 처리" --force
```

`--force`는 동명 라벨(GitHub 기본 라벨 등)이 있을 때 덮어쓴다. 색상 코드는 참고용 배정(role=파랑, status=초록/노랑/빨강, priority=주황·노랑·연두)이며 팀 취향대로 바꿔도 무방하다.

### (B) 웹 UI

1. 저장소 → **Settings** → **Labels** (`https://github.com/iejunkimu/lg-home-ai-team/labels`)
2. **New label** 클릭 → `.github/labels.md`의 각 행을 이름/설명/색상 그대로 입력 → **Create label**
3. 총 11개 라벨(role 4 + status 4 + priority 3) 생성될 때까지 반복
4. 필요 없는 GitHub 기본 라벨(`bug`, `enhancement` 등)은 지워도 되고 남겨둬도 됨 — 팀 판단

---

## 2. Projects 칸반 보드 생성 + 아이디어 5개 이슈화

### 2-1. 아이디어 5건을 이슈로 등록

`docs/ideas/`의 5개 문서를 각각 이슈로 만든다. 템플릿은 `.github/ISSUE_TEMPLATE/idea.md`.

대상 문서:
- `docs/ideas/ai-virtual-zoning.md`
- `docs/ideas/냉장고-erp-서비스.md`
- `docs/ideas/베이비-제로-터치-로그.md`
- `docs/ideas/스마트옷장.md`
- `docs/ideas/유럽-타겟팅-에어컨-시스템.md`

#### (A) `gh` 명령 (재인증 후)

```bash
gh issue create --title "[아이디어] AI Virtual Zoning" \
  --body-file docs/ideas/ai-virtual-zoning.md \
  --label "role: ai,status: 제안"

gh issue create --title "[아이디어] 냉장고 ERP 서비스(재고관리)" \
  --body-file docs/ideas/냉장고-erp-서비스.md \
  --label "role: ai,status: 제안"

gh issue create --title "[아이디어] 베이비 제로터치 로그" \
  --body-file docs/ideas/베이비-제로-터치-로그.md \
  --label "role: ai,status: 제안"

gh issue create --title "[아이디어] 스마트옷장" \
  --body-file docs/ideas/스마트옷장.md \
  --label "role: ai,status: 제안"

gh issue create --title "[아이디어] 유럽 타겟팅 에어컨 시스템" \
  --body-file docs/ideas/유럽-타겟팅-에어컨-시스템.md \
  --label "role: ai,status: 제안"
```

> 참고: `docs/process/_notion-recovery-index.md`에 이미 각 아이디어의 Notion 상 상태(보관됨/추가 정보 필요/거부됨 등)가 기록돼 있다. 이슈 등록 시 `status:` 라벨을 그 상태에 맞춰 조정할지는 팀 판단 — 위 명령은 기본값으로 전부 `status: 제안`을 달았다.

#### (B) 웹 UI

1. 저장소 → **Issues** 탭 → **New issue** → "아이디어 제안" 템플릿 선택
2. 제목을 `[아이디어] <이름>` 형식으로, 본문은 `docs/ideas/<파일>.md` 내용을 참고해 채운다 (또는 파일 링크만 걸고 "상세는 docs/ideas/... 참고"로 축약해도 됨 — 팀 판단)
3. 5개 아이디어 각각 반복

### 2-2. Projects 보드 생성

#### (A) `gh` 명령

```bash
gh project create --owner iejunkimu --title "LG Home AI 팀 프로젝트"
# 생성된 프로젝트 번호 확인
gh project list --owner iejunkimu
# 이슈를 보드에 추가 (프로젝트 번호는 위 명령 결과로 확인한 번호로 교체)
gh project item-add <프로젝트번호> --owner iejunkimu --url https://github.com/iejunkimu/lg-home-ai-team/issues/<이슈번호>
```

#### (B) 웹 UI

1. 저장소 → **Projects** 탭 → **New project** → 템플릿 "Board" 선택
2. 컬럼 구성: `제안` → `토론중` → `채택` / `기각` (`.github/labels.md`의 `status:` 라벨과 대응)
3. 위에서 만든 이슈 5개를 보드에 추가 (Add item → 검색해서 연결)
4. 이후 새 이슈도 생성 시 자동으로 보드에 들어오게 하려면 프로젝트 **Workflows** 설정에서 "Auto-add to project" 활성화

---

## 3. `main` 브랜치 보호 규칙

PR 필수 + 리뷰 1명 이상 승인 + `main` 직접 push 금지를 GitHub 설정으로 강제한다 (지금까지는 `CONTRIBUTING.md` 문서 규범일 뿐, 기술적으로 막혀있지 않음).

### (A) `gh` 명령

```bash
gh api repos/iejunkimu/lg-home-ai-team/branches/main/protection \
  --method PUT \
  --input - <<'EOF'
{
  "required_status_checks": null,
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1
  },
  "restrictions": null,
  "required_linear_history": false,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

### (B) 웹 UI

1. 저장소 → **Settings** → **Branches**
2. **Branch protection rules** → **Add branch protection rule**
3. Branch name pattern: `main`
4. 체크:
   - ☑ **Require a pull request before merging**
   - ☑ **Require approvals** → 최소 1
   - ☑ **Do not allow bypassing the above settings** (관리자도 예외 없이 적용하려면)
5. **Create** / **Save changes**

> 참고: 위 설정을 켜면 `git push origin main` 직접 push가 실제로 거부된다. 지금까지 이 문서 자체를 포함한 초기 커밋들은 이 보호 규칙이 켜지기 전에 만든 것이므로, 이 규칙 적용 이후부터 실제로 GitHub Flow가 강제된다.

---

## 3.5. GitHub Pages 소스 = "GitHub Actions"

MkDocs Material 빌드·배포는 이미 배선됨 (`mkdocs.yml` + `.github/workflows/deploy.yml` + `requirements.txt`, `docs/methodology/toolchain.md` § 5 참고). `main`에 push할 때마다 자동으로 빌드·배포되지만, Pages 자체가 어느 소스를 쓸지는 저장소 설정에서 한 번 지정해야 한다.

1. 저장소 → **Settings** → **Pages**
2. **Build and deployment → Source**를 "Deploy from a branch"에서 **"GitHub Actions"**로 변경
3. `main`에 다음 push가 일어나면 워크플로가 자동 실행되고, 완료 후 `https://iejunkimu.github.io/lg-home-ai-team/`에서 확인 가능

---

## 4. Obsidian · Obsidian Git · Dataview 플러그인 설치

`docs/methodology/toolchain.md` § 1~2 상세 참고. 각 팀원이 로컬에서 진행.

1. **Obsidian 설치**: https://obsidian.md 에서 앱 다운로드·설치
2. **이 레포를 vault로 열기**: Obsidian 실행 → "Open folder as vault" → 로컬에 클론된 `lg-home-ai-team` 폴더 선택
3. **Obsidian Git 플러그인 설치**: 설정(Settings) → Community plugins → Browse → "Obsidian Git" 검색 → Install → Enable
4. **Dataview 플러그인 설치**: 같은 경로에서 "Dataview" 검색 → Install → Enable
5. 확인: `docs/ideas/` 아래 문서를 열어 frontmatter(`status` 등)가 보이는지 확인하고, 필요하면 `docs/methodology/toolchain.md`의 예시 Dataview 쿼리(`TABLE status, votes FROM "docs/ideas" SORT votes DESC`)를 새 노트에 붙여넣어 정상 렌더되는지 테스트

> gh/웹 UI 구분 없음 — 순수 로컬 앱 설치이므로 각자 진행.

---

## 남은 일 요약

- [ ] `gh auth login -h github.com` 재인증
- [ ] 라벨 11개 생성 (§ 1)
- [ ] 아이디어 5건 이슈 등록 (§ 2-1)
- [ ] Projects 칸반 보드 생성 + 이슈 연결 (§ 2-2)
- [ ] `main` 브랜치 보호 규칙 설정 (§ 3)
- [ ] GitHub Pages Source를 "GitHub Actions"로 설정 (§ 3.5 — 나머지는 이미 배선됨)
- [ ] 팀원 각자 Obsidian + Obsidian Git + Dataview 설치 (§ 4)
- [ ] **팀 판정 대기 (ARCHITECTURE.md § 6 참고, 여기서 확정하지 않음)**:
  - Conventional Commits 타입 집합 · scope 강제 여부 · commitlint 등 강제 도구 도입 여부
  - 브랜치 전략: GitHub Flow 유지 vs trunk-based 전환
