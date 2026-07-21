---
title: "냉장고 ERP 서비스(재고관리)"
notion_page_id: "38e7e94f-06e9-80d5-a28a-cf0828541db0"
notion_url: "https://app.notion.com/p/38e7e94f06e980d5a28acf0828541db0"
last_edited: "2026-07-15T09:37:43.297Z"
recovered_date: "2026-07-21"
status: "토론 중"
---

# 냉장고 ERP 서비스(재고관리)

## 아이디어 설명

주방을 하나의 **스마트 팩토리**로 정의해 냉장고·후드·인덕션을 AI로 연동, 재고 관리·환경 제어·자동 조리·영양 코칭까지 제공하는 통합 플랫폼입니다. 사용자는 최소한의 개입만으로 메뉴 추천과 재고 차감, 맞춤형 건강 식단을 경험할 수 있습니다.

---

## 왜 중요한가

- **사용자 가치:** 메뉴 고민과 조리 피로를 줄이고 영양 균형을 챙겨줌
- **기업 가치:** 하드웨어 판매를 넘어 커머스·헬스케어 구독으로 확장
- **전략적 가치:** LG ThinQ 생태계와 결합해 강력한 락인 효과 확보

---

## 뒷받침 데이터

(데이터 섹션은 Notion에서 비어있음)

---

## 경쟁사

(이미지 참고 - 원본 Notion 문서의 이미지 URL 포함)

---

## 전문가 피드백

### 자사 제품과 겹치는가 — 정면으로 걸림

- LG InstaView ThinQ가 컴퓨터 비전+LLM으로 식재료 인식·식단 제안을 이미 상용화했다.
- 삼성 Family Hub도 2025년 신선 37종+포장 50종 인식에 Gemini를 탑재했다.
- LG 심사 앞에서는 "LG가 이미 파는 것을 다시 만들자"는 제안이 된다.

### 데이터를 확보할 수 있는가

**막히지 않는다.**

- 일반 음식 인식 데이터는 10만 장 이상으로 풍부하고
- 냉장고 내부 전용 데이터는 상대적으로 적지만(Roboflow Universe의 소규모 공개셋 수준 — 수천 장대) 다른 데이터로 보강 가능하다.
- 즉 이 후보의 문제는 데이터가 아니다.

### 일반 음식 인식 데이터(풍부)

- Food-101: https://huggingface.co/datasets/ethz/food101

### 냉장고 CV 상용 파이프라인화

https://www.basic.ai/blog-post/computer-vision-for-smart-fridges-how-it-works-models-data-and-annotations

### 삼성 Family Hub 2025(신선 37종+포장 50종 인식·Gemini 탑재)

https://news.samsung.com/us/samsung-family-hub-2025-update-elevates-smart-home-ecosystem

### LG·삼성 식재료 인식 냉장고(CES 전시)

https://thespoon.tech/lg-and-samsung-to-show-off-new-food-identifying-smart-fridges-at-ces-next-week/

### 냉장고 내부 전용 공개 데이터(소규모)

- Roboflow Universe 예: Whatsinyourfridge 9,777장
- Northumbria Smart Refrigerator 3,049장
