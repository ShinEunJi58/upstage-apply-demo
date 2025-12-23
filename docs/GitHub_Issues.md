# GitHub Issues Draft (Python/Streamlit Version)
> GitHub CLI(`gh`)가 설치되어 있지 않아 자동 등록할 수 없습니다. 아래 내용을 복사하여 이슈를 생성해주세요.

---

## Epic 1-2: Data Schema Design (데이터 설계)

### [Issue] 운임 비교용 정형 데이터(Excel) 스키마 정의
*   **Epic**: Data Schema Design
*   **Task ID**: Task 1-2-1
*   **작업 배경 (Background)**
    Streamlit 앱에서 사용자에게 운임 비교 결과를 보여주기 위해, Pandas DataFrame으로 로드할 로우 데이터의 구조를 정의해야 함.
*   **작업 내용 (Description)**
    *   `Route` (NSR/Suez), `Distance` (km), `Lead_Time` (days), `Fuel_Cost_Index`, `Container_Cost` 등의 컬럼을 포함한 엑셀(.xlsx) 또는 CSV 스키마 설계.
    *   Streamlit 차트 시각화에 적합한 데이터 타입(Float/Int) 정의.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] `pd.read_excel()`로 로드했을 때 오류가 없는 샘플 파일(`route_data_sample.xlsx`)이 생성되어야 한다.

### [Issue] 품목 추천용 비정형 데이터(Markdown/PDF) 구조 설계
*   **Epic**: Data Schema Design
*   **Task ID**: Task 1-2-2
*   **작업 배경 (Background)**
    RAG(Retrieval-Augmented Generation) 시스템이 문서를 잘 검색할 수 있도록 Markdown 문서의 헤더 구조를 표준화해야 함.
*   **작업 내용 (Description)**
    *   K-Food, K-Beauty 등 카테고리별 유망 품목 리스트의 문서 구조 정의.
    *   Markdown 헤더 구조(# 품목명, ## 특징, ## 추천 이유) 표준화.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] LangChain `MarkdownHeaderTextSplitter`로 분할하기 용이한 포맷의 샘플 문서가 작성되어야 한다.

### [Issue] 시스템 프롬프트(System Prompt) 초안 작성
*   **Epic**: Data Schema Design
*   **Task ID**: Task 1-2-3
*   **작업 배경 (Background)**
    LangChain의 ChatModel에 주입할 시스템 메시지(System Message)를 설계하여 AI의 페르소나를 설정함.
*   **작업 내용 (Description)**
    *   역할 정의: "너는 KOTRA의 10년차 무역 전문가야."
    *   톤앤매너(Tone & Manner): 전문적이고 신뢰감 있는 말투.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] `prompt.txt` 파일에 시스템 프롬프트 내용이 작성되어야 한다.

---

## Phase 2: Data Preparation (데이터 준비)

### [Issue] 가상의 부산-함부르크 운임 비교 데이터 생성
*   **Epic**: Structured Data Construction
*   **Task ID**: Task 2-1-1
*   **작업 배경 (Background)**
    앱 시연에 사용할 더미 데이터를 생성함.
*   **작업 내용 (Description)**
    *   부산 -> 함부르크 구간의 수에즈 운하 vs 북극항로 운항 데이터 생성.
    *   비교 차트를 그렸을 때 북극항로의 장점(거리 단축)이 잘 드러나도록 데이터셋 구성.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] `data/shipping_cost.csv` 파일이 생성되고 10개 이상의 Row가 존재해야 한다.

### [Issue] Python 데이터 처리 테스트
*   **Epic**: Structured Data Construction
*   **Task ID**: Task 2-1-2
*   **작업 배경 (Background)**
    Streamlit 앱 개발 전, 데이터 로드 및 간단한 연산 로직을 미리 검증함.
*   **작업 내용 (Description)**
    *   Jupyter Notebook 또는 스크립트로 CSV 파일 로드 테스트.
    *   기본적인 필터링 및 그룹화 연산 수행.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] `test_data_loading.py` 실행 시 에러 없이 데이터프레임 정보가 출력되어야 한다.

---

## Phase 3: Application Development (앱 개발)

### [Issue] Python 가상환경 생성 및 필요 라이브러리 설치
*   **Epic**: Environment Setup
*   **Task ID**: Task 3-1-1
*   **작업 배경 (Background)**
    프로젝트 의존성을 관리하기 위해 가상환경을 세팅함.
*   **작업 내용 (Description)**
    *   `venv` 또는 `conda` 가상환경 생성.
    *   `streamlit`, `langchain`, `openai`, `pandas`, `openpyxl` 등 필수 패키지 설치.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] `requirements.txt` 파일이 생성되어야 한다.
    *   [ ] `streamlit hello` 명령어가 정상 작동해야 한다.

### [Issue] [NSR Cost Calculator] Pandas 기반 운임 계산 함수 구현
*   **Epic**: Core Feature Implementation
*   **Task ID**: Task 3-2-1
*   **작업 배경 (Background)**
    사용자 입력(출발/도착/물량)을 받아 비용 절감액을 계산해주는 핵심 로직 개발.
*   **작업 내용 (Description)**
    *   Pandas DataFrame을 필터링하여 해당 구간의 운임 정보 추출 함수 작성.
    *   절감액 및 절감 시간 계산 로직 구현.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] 입력값에 따라 북극항로 vs 수에즈항로 비교 수치가 정확히 리턴되어야 한다.

### [Issue] [Item Matcher] RAG 파이프라인 구축
*   **Epic**: Core Feature Implementation
*   **Task ID**: Task 3-2-2
*   **작업 배경 (Background)**
    사용자 질문에 맞는 유망 품목을 추천하기 위해 벡터 검색 시스템을 구축함.
*   **작업 내용 (Description)**
    *   문서 로드 -> 텍스트 분할(Split) -> 임베딩 -> 벡터 저장소(FAISS/Chroma) 저장 흐름 구현.
    *   LangChain `RetrievalQA` 체인 구성.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] "화장품 추천해줘" 질문 시 관련 문서 청크가 검색되어야 한다.

### [Issue] Streamlit Chat UI 기본 레이아웃 구성
*   **Epic**: UI Implementation
*   **Task ID**: Task 3-3-1
*   **작업 배경 (Background)**
    사용자가 챗봇과 대화할 수 있는 웹 인터페이스를 구현함.
*   **작업 내용 (Description)**
    *   `st.set_page_config`로 페이지 타이틀 설정.
    *   `st.chat_message`와 `st.chat_input`을 활용한 대화창 UI 구현.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] 웹 브라우저에서 채팅창이 보이고, 메시지를 입력하면 화면에 표시되어야 한다.

---

## Phase 4: Verification & Deployment (검증 및 배포)

### [Issue] Streamlit Cloud 배포 테스트
*   **Epic**: Testing
*   **Task ID**: Task 4-1-2
*   **작업 배경 (Background)**
    로컬에서 개발한 앱이 클라우드 환경에서도 정상 작동하는지 확인.
*   **작업 내용 (Description)**
    *   Streamlit Community Cloud에 리포지토리 연동 및 배포.
    *   `secrets.toml` (API Key) 설정.
*   **인수 조건 (Acceptance Criteria)**
    *   [ ] 외부에서 접속 가능한 URL이 생성되고 에러 없이 접속되어야 한다.
