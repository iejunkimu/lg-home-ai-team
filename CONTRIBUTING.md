# 협업 규칙 (CONTRIBUTING)

이 레포에서 작업하기 전에 읽는다. 더 자세한 배경·예시는 `docs/methodology/git-github-협업.md`에 있다.

> **현재 상태: 초기 운영 초안.** GitHub Flow를 안전한 출발값으로 사용하고 있지만, review·merge 주체와 강제 수준은 팀이 [`GitHub 거버넌스 토론 초안`](docs/methodology/github-governance-draft.md)을 보고 판정한 뒤 확정한다.

## 기본 흐름 — GitHub Flow

현재 출발값으로 GitHub 공식 [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) 6단계를 따른다.

1. `main`에서 새 브랜치를 판다
2. 커밋한다 (Conventional Commits 형식)
3. Pull Request를 연다
4. 리뷰를 받고 반영한다
5. 승인 후 머지한다
6. 브랜치를 지운다

## 브랜치 명명

```
feature/짧은-설명    새 기능
fix/짧은-설명         버그 수정
docs/짧은-설명        문서 작업
chore/짧은-설명       설정·잡무
```

예: `feature/refrigerator-cv-model`, `docs/idea-selection-criteria`

## 커밋 메시지 — Conventional Commits

[Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) 형식을 쓴다:

```
<type>: <description>
```

주로 쓰는 type: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.

예: `feat(fridge): 무게 센서 기반 재고 차감 로직 추가`

여러 명이 같이 만든 커밋이면 트레일러를 추가한다:

```
Co-authored-by: 이름 <GitHub이메일>
```

## PR 규칙 — 현재 제안값

- **리뷰어 1명 이상의 승인 없이 머지하지 않는다.**
- **`main`에 직접 push하지 않는다** — 모든 변경은 PR을 통해서만 넣는다.
- PR 설명에는 무엇을 바꿨고 왜 바꿨는지 적는다. 관련 이슈가 있으면 `Closes #번호`로 링크한다.
- PR 템플릿(`.github/PULL_REQUEST_TEMPLATE.md`)의 항목(무엇을 바꿨나 / 왜 / 테스트 방법 / 관련 이슈)을 채운다.

위 두 항목은 branch protection으로 강제된 상태인지 아직 확인되지 않았다. 오늘 팀이 운영안을 고르기 전까지의 안전한 기본값이며, 확정 뒤 이 절을 팀 판정에 맞게 갱신한다.

`docs/`는 merge 뒤 공개 Pages의 navigation과 검색에 자동 포함된다. 개인 초안·개인정보·비밀값처럼 공개 준비가 안 된 내용은 `docs/`에 넣지 않는다.

## 순서와 노출 — 완성본을 먼저 던지지 않는다

이 항목은 GitHub가 강제하는 규칙이 아니라 **우리 팀이 정한 협업 규범**이다.

완성된 결과물을 통째로 던지면 다른 팀원이 스스로 문제를 탐색하고 소유감을 가질 기회가 사라진다. 그래서:

1. 하루 이상 걸릴 작업은 코드를 다 짜기 전에 **이슈나 Draft PR로 문제·질문·뼈대를 먼저 공유**한다.
2. 다른 팀원이 그걸 보고 **독립적으로 자기 의견을 형성할 시간**을 준다.
3. 완성된 답은 그 다음이다.

브랜치는 독립적으로 탐색하는 공간이고, PR은 의도적으로 팀에게 보여주기로 결정한 지점이다. 다 만든 뒤에만 PR을 여는 게 기본이 아니다 — 뼈대만 있는 상태에서 Draft PR로 먼저 여는 것도 정상이다.

자세한 설명은 `docs/methodology/git-github-협업.md` § 5를 참고한다.

## 이슈 템플릿

- 아이디어 제안: `.github/ISSUE_TEMPLATE/idea.md`
- 작업(Task): `.github/ISSUE_TEMPLATE/task.md`

라벨 체계는 `.github/labels.md` 참고.
