# 라벨 목록

이슈/PR에 붙이는 라벨 체계. GitHub 저장소 Settings → Labels에서 아래 표대로 생성해 사용한다.

## 역할 (role)

| 라벨 | 의미 |
|---|---|
| `role: ai` | AI·데이터 모델링 관련 |
| `role: backend` | 백엔드·IoT 통신 관련 |
| `role: frontend` | 프론트엔드·앱 UI 관련 |
| `role: docs` | 문서·기획 관련 |

## 상태 (status)

| 라벨 | 의미 |
|---|---|
| `status: 제안` | 새로 제안됨, 아직 논의 전 |
| `status: 토론중` | 팀 논의가 진행 중 |
| `status: 채택` | 팀이 채택하기로 결정 |
| `status: 기각` | 팀이 채택하지 않기로 결정 (근거는 이슈 코멘트에 남긴다) |

## 우선순위 (priority)

| 라벨 | 의미 |
|---|---|
| `priority: high` | 이번 스프린트 내 처리 필요 |
| `priority: med` | 가까운 시일 내 처리 |
| `priority: low` | 여유 있을 때 처리 |

---

라벨은 `role:`, `status:`, `priority:` 세 그룹으로 구분해서 색상도 그룹별로 통일해두면(예: role=파랑 계열, status=초록/빨강 계열, priority=노랑 계열) 이슈 목록에서 한눈에 구분하기 쉽다.
