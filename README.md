---
title: NSR Smart Navigator
emoji: 🚢
colorFrom: blue
colorTo: cyan
sdk: streamlit
sdk_version: 1.31.0
app_file: app.py
pinned: false
---

# NSR Smart Navigator - 북극항로 수출 전략 에이전트

**NSR Smart Navigator**는 복잡한 북극항로(NSR: Northern Sea Route) 물류 데이터를 AI 에이전트가 실시간으로 분석하여, 유럽 수출을 희망하는 중소기업에게 최적의 물류 경로와 리스크 정보를 대화형으로 제공하는 서비스입니다.

KOTRA의 핵심 업무인 **'시장 정보 조사'**와 **'해외진출 지원'** 업무의 디지털 전환(DX) 예시를 시각적으로 구현하여, 무역 업무의 효율성을 극대화하는 것을 목표로 합니다.

![Project Status](https://img.shields.io/badge/Status-Prototype-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red)

---

## 🚀 주요 기능 (Key Features)

### 1. 💰 경제성 진단 (NSR Cost Calculator)
- 기존 수에즈 운하 항로 대비 북극항로 이용 시의 거리, 소요 시간(Lead Time), 연료 절감액을 비교 분석합니다.
- 사용자의 화물 컨테이너 수와 목적지에 따른 예상 비용 절감 효과를 시뮬레이션합니다.

### 2. ⚠️ 리스크 모니터링 (Risk Radar)
- 북극 해빙 농도 데이터와 러시아-우크라이나 지정학적 이슈를 종합하여 **[안전 / 주의 / 위험]** 신호등 형태로 보여줍니다.
- 실시간 뉴스 데이터를 기반으로 운항 가능 여부를 진단합니다.

### 3. 📦 수출 유망 품목 추천 (Item Matcher)
- 빠른 배송이 핵심 경쟁력인 상품(신선식품, 패스트패션 등)을 AI가 추천합니다.
- 북극항로 이용 시 이점이 극대화되는 품목군을 제안합니다.

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language**: Python 3.11+
- **Web Framework**: Streamlit
- **Data Processing**: Pandas
- **Visualization**: Plotly
- **AI/LLM**: (예정) LangChain, OpenAI GPT-4

---

## 💻 실행 방법 (Getting Started)

### 1. 환경 설정
Python 3.11 이상이 필요합니다.

```bash
# 가상환경 생성 및 실행
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 앱 실행
```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501`로 접속하여 확인합니다.

---

## 📂 프로젝트 구조

```
upstage-apply-demo/
├── app.py                  # 메인 애플리케이션 진입점
├── requirements.txt        # 프로젝트 의존성 라이브러리
├── data/                   # 데이터 파일 (CSV 등)
├── docs/                   # 기획 및 설계 문서 (PRD 등)
└── README.md               # 프로젝트 설명서
```

---

## 📝 라이선스
This project is for demonstration purposes only.
