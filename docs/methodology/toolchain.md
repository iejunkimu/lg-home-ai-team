# 저장층(Storage Stack) 셋업 가이드 — Notion → GitHub 이주

Notion에서 하던 일을 GitHub/markdown 기반으로 그대로(또는 더 낫게) 하기 위한 도구 조합이다. 각 항목은 "무엇을 대체하는지"와 "설치가 필요한지"를 기준으로 정리했다.

## 한눈에 보는 표

| 기능 | 도구 | Notion에서 하던 일 | 설치 필요 여부 |
|---|---|---|---|
| 저작(글쓰기) | GitHub 웹 또는 원하는 markdown 편집기 | 페이지 작성/편집 | GitHub 웹은 설치 없음 |
| 로컬 DB 뷰 | Dataview (Obsidian 플러그인) | Notion 데이터베이스 뷰(표/칸반) | 플러그인 설치 |
| 팀 DB / 투표 | GitHub Issues + Projects | Notion DB의 아이디어 목록·투표·상태 | 없음 (GitHub 내장) |
| 다이어그램 | Mermaid | Notion 임베드 다이어그램 | 없음 (GitHub·Obsidian 네이티브 렌더) |
| 게시/렌더 | Quartz 또는 MkDocs Material / GitHub Pages / GitHub Wiki | Notion 공개 페이지 뷰 | 정적 사이트 생성기 설치(택1), Pages/Wiki는 설정만 |
| 이미지 | 레포 `assets/` | Notion 파일 업로드 | 없음 |

---

## 1. 저작 — GitHub 웹부터, 로컬 도구는 선택

GitHub가 처음인 팀원은 GitHub 웹에서 markdown 파일을 수정하고 PR을 여는 것만으로 시작할 수 있다. **Obsidian·Dataview·CLI 설치는 첫 PR의 선결 조건이 아니다.**

문서를 자주 쓰거나 로컬에서 편집하고 싶은 팀원은 Obsidian을 선택할 수 있다. Obsidian은 로컬 markdown 파일을 그대로 다루는 노트 앱이라 git 레포와 궁합이 좋다.

**Obsidian Git 플러그인**을 설치하면 일정 주기로 자동 커밋/푸시를 해주거나, 단축키 한 번으로 add-commit-push를 묶어서 실행할 수 있다. 팀원이 git 명령어에 아직 익숙하지 않을 때 진입장벽을 낮추는 용도다. (단, `docs/methodology/git-github-협업.md`의 커밋 메시지 규약과 브랜치 규범은 자동 커밋을 쓰더라도 동일하게 지킨다 — 자동 커밋 메시지를 그대로 두지 말고 의미 있는 메시지로 고쳐 쓰는 습관을 들인다.)

- 설치: Obsidian → 커뮤니티 플러그인 → "Obsidian Git" 검색 후 설치
- 이 레포를 Obsidian vault로 열면 바로 사용 가능

## 2. 로컬 DB 뷰 — Dataview

Notion 데이터베이스의 "속성별 필터링된 표/칸반 뷰"를 대체한다. markdown 파일의 YAML frontmatter(예: `status`, `votes`, `priority`)를 인덱싱해서 쿼리 결과를 표나 리스트로 보여준다.

예시 — `docs/ideas/` 아래 파일들을 상태별로 모아보는 쿼리:

````
```dataview
TABLE status, votes
FROM "docs/ideas"
SORT votes DESC
```
````

- 설치: Obsidian 커뮤니티 플러그인 → "Dataview" 검색 후 설치
- 전제조건: 각 문서 frontmatter에 `status`, `votes` 같은 필드가 일관되게 있어야 쿼리가 의미 있다. 현재 이관된 idea 문서들은 Notion 원본 frontmatter(`status` 등)를 보존하고 있다 — 새 문서를 쓸 때도 같은 필드명을 맞춰 쓴다.

## 3. 팀 DB / 투표 — GitHub Issues + Projects

Notion에서 "아이디어 하나 = row 하나, 투표 = 속성"으로 관리하던 것을 GitHub 네이티브 기능으로 옮긴다.

- **아이디어 = 이슈 하나.** `.github/ISSUE_TEMPLATE/idea.md` 템플릿으로 새 아이디어를 이슈로 연다.
- **투표 = 👍 리액션.** 이슈 본문에 팀원이 👍를 누르면 그게 투표다. GitHub Issues 목록은 리액션 개수로 정렬할 수 있다.
- **카테고리/상태 = 라벨.** `.github/labels.md`에 정리된 라벨(역할별/상태별/우선순위별)을 이슈에 붙인다.
- **칸반 = GitHub Projects.** 저장소 상단 "Projects" 탭에서 보드를 만들고, 이슈를 상태별 컬럼(제안 → 토론중 → 채택/기각)으로 옮긴다. Notion의 칸반 뷰와 동일한 사용 경험이다.

설치 불필요 — 전부 GitHub 웹에 내장된 기능이다.

## 4. 다이어그램 — Mermaid

시스템 구조도, 시나리오 플로우(예: `docs/ideas/ai-virtual-zoning.md`의 "생활 전환 지원" 흐름도) 등을 텍스트로 그린다.

````
```mermaid
flowchart LR
  A[집중 종료 감지] --> B[업무 화면 알림 정리]
  B --> C[책상 조명 감소]
  C --> D[침대 조명·음향 활성화]
```
````

GitHub는 markdown 안의 ` ```mermaid ` 코드블록을 웹에서 자동으로 렌더링한다. Obsidian도 동일 문법을 네이티브로 지원한다. 별도 설치가 필요 없다 — 둘 다 기본 지원.

## 5. 게시/렌더 — 현재 운영판

현재 운영판은 **MkDocs Material로 빌드하고 GitHub Pages로 배포**한다.

- Pull Request: `.github/workflows/validate-docs.yml`이 전체 문서를 `mkdocs build --strict`로 검사한다.
- `main` merge: `.github/workflows/deploy.yml`이 사이트를 다시 빌드해 Pages에 배포한다.
- navigation: `mkdocs.yml`에 수동 목록을 두지 않는다. 따라서 `docs/` 아래 새 markdown도 자동으로 탐색 메뉴와 검색에 포함된다.
- 배포 확인: Pages 배포 뒤 모든 문서의 공개 URL과 navigation 링크를 다시 검사한다.
- 공개 주소: `https://iejunkimu.github.io/lg-home-ai-team/`

Quartz나 GitHub Wiki는 현재 운영판이 아니다. 필요가 생기면 팀 판정으로 다시 검토한다.

!!! warning "`docs/`는 공개 영역"
    이 레포와 Pages는 공개돼 있다. `docs/`에 넣고 merge한 파일은 자동으로 navigation과 검색에 나타난다. 팀에 아직 공개할 준비가 안 된 개인 초안·개인정보·비밀값은 `docs/`에 넣지 않는다.

## 6. 이미지 — 레포 `assets/`

Notion은 이미지 업로드 시 presigned S3 URL을 발급하는데, 이 URL은 일정 시간 후 만료된다(이번 이주 작업 중 실제로 `docs/ideas/냉장고-erp-서비스.md`에서 이 문제로 원본 이미지 URL을 살리지 못했다). 이 문제를 근본적으로 없애기 위해 이미지는 **레포 안에 직접 저장**한다.

- 이미지 파일은 `assets/`에 넣는다 (하위 폴더로 주제별 정리 가능, 예: `assets/ideas/`, `assets/process/`).
- markdown에서는 상대경로로 참조한다: `![설명](../../assets/ideas/파일명.png)`
- 대용량 이미지·동영상은 `.gitignore`에 걸리지 않는지 확인하고, 너무 크면 Git LFS 도입을 검토한다 (현재는 불필요 — 문서량이 적음).

설치 불필요 — 그냥 폴더에 파일을 넣으면 된다.

---

## 선택해서 설치할 수 있는 것

- **Obsidian** (로컬 markdown 저작이 필요할 때)
- **Obsidian Git** 플러그인 (Obsidian에서 Git 작업을 하고 싶을 때)
- **Dataview** 플러그인 (로컬 DB 뷰가 필요할 때)

나머지(GitHub 웹 편집, Issues/Projects/labels, Mermaid, GitHub Pages, `assets/` 폴더)는 별도 설치가 없다. MkDocs는 Pages workflow가 설치하므로 팀원 개인 설치가 필수는 아니다.
