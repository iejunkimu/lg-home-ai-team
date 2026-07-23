# LG Home AI 팀플

이 사이트는 [`lg-home-ai-team`](https://github.com/iejunkimu/lg-home-ai-team) 레포의 `docs/`를 그대로 렌더링한 것이다. 정본은 항상 레포 markdown — 여기는 읽기용 게시 뷰.

- **프로세스** — 아이디어를 어떻게 짜고 고르는지 (설계 프로세스, 선택 기준, 회의록)
- **아이디어** — `docs/ideas/`의 후보·조사 문서
- **방법론** — 협업 도구 셋업 가이드 (git/GitHub, toolchain)

전체 그림과 구조 이유는 레포 루트 [`ARCHITECTURE.md`](https://github.com/iejunkimu/lg-home-ai-team/blob/main/ARCHITECTURE.md) 참고.

## 문서 게시 방식

`docs/` 아래 markdown은 `main`에 merge되면 GitHub Pages에 자동 게시되고 검색·탐색 메뉴에도 포함된다. 새 문서를 추가할 때 `mkdocs.yml`의 메뉴를 따로 수정할 필요가 없다.

Pull Request에서는 먼저 전체 문서 빌드와 navigation을 검사한다. 실제 공개 배포는 `main`에 merge된 뒤에만 실행하며, 배포 뒤에는 각 문서의 공개 URL과 navigation을 다시 확인한다.
