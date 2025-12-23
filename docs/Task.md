# Project Task List
## NSR Smart Navigator Project

| 항목 | 내용 |
| --- | --- |
| **프로젝트명** | NSR Smart Navigator |
| **문서 목적** | 프로젝트 진행 단계별 세부 작업 관리 (Python/Streamlit Ver.) |
| **작성일** | 2024-12-22 |

---

## Phase 1: Planning & Design (기획 및 설계)
> 프로젝트의 방향성을 설정하고 필요한 요구사항과 기술 스택을 정의합니다.

### Epic 1-1: Requirement Analysis (요구사항 분석)
- [x] **Task 1-1-1**: `docs/ideation.md` 분석 및 핵심 기능 도출
- [x] **Task 1-1-2**: `docs/PRD.md` 작성 (핵심 기능, 타겟 유저, 페르소나 정의)
- [x] **Task 1-1-3**: `docs/TechStack.md` 작성 (Python, Streamlit, LangChain 선정)

### Epic 1-2: Data Schema Design (데이터 설계)
- [x] **Task 1-2-1**: 운임 비교용 정형 데이터(Excel) 스키마 정의 (`Route`, `Distance`, `Cost`, `Time` 등)
- [ ] **Task 1-2-2**: 품목 추천용 비정형 데이터(Markdown/PDF) 구조 설계
- [ ] **Task 1-2-3**: 시스템 프롬프트(System Prompt) 초안 작성 (페르소나 설정)

---

## Phase 2: Data Preparation (데이터 준비)
> 에이전트가 학습할 Knowledge Base 데이터를 실제 파일로 제작합니다.

### Epic 2-1: Structured Data Construction (정형 데이터 구축)
- [ ] **Task 2-1-1**: 가상의 부산-함부르크 운임 비교 데이터 생성 (Pandas 로드용 CSV/Excel)
- [ ] **Task 2-1-2**: Python 데이터 처리 테스트 (데이터 로드 및 연산 검증)

### Epic 2-2: Unstructured Data Construction (비정형 데이터 구축)
- [ ] **Task 2-2-1**: 유럽 수출 유망 품목(K-Food, K-Beauty 등) 리스트整理
- [ ] **Task 2-2-2**: 품목별 HS Code 및 관세 팁 자료 수집 및 문서화 (RAG 문서 구축)

---

## Phase 3: Application Development (앱 개발)
> Streamlit과 LangChain을 활용하여 실제 애플리케이션을 개발합니다.

### Epic 3-1: Environment Setup (환경 설정)
- [ ] **Task 3-1-1**: Python 가상환경 생성 및 필요 라이브러리 설치 (`streamlit`, `langchain`, `openai`, `pandas` 등)
- [ ] **Task 3-1-2**: GitHub 리포지토리 초기화 및 `.gitignore` 설정

### Epic 3-2: Core Feature Implementation (핵심 기능 구현)
- [ ] **Task 3-2-1**: **[NSR Cost Calculator]** Pandas 기반 운임 계산 함수 구현
- [ ] **Task 3-2-2**: **[Item Matcher]** RAG(Retrieval) 파이프라인 구축 (Vector DB 연동)
- [ ] **Task 3-2-3**: **[Risk Radar]** LangChain Web Search Tool(Tavily/Google) 연동

### Epic 3-3: UI Implementation (UI 구현)
- [ ] **Task 3-3-1**: Streamlit Chat UI 기본 레이아웃 구성
- [ ] **Task 3-3-2**: 사용자 의도(Intent)에 따른 툴 라우팅 로직 구현 (LLM Function Calling)

---

## Phase 4: Verification & Deployment (검증 및 배포)
> 구현된 에이전트를 테스트하고 최종 산출물로 배포합니다.

### Epic 4-1: Testing (테스트)
- [ ] **Task 4-1-1**: 시나리오 테스트 (운임 문의, 리스크 문의, 추천 문의)
- [ ] **Task 4-1-2**: Streamlit Cloud 배포 테스트
- [ ] **Task 4-1-3**: 답변 정확도 검증 및 프롬프트 튜닝

### Epic 4-2: Launch (배포)
- [ ] **Task 4-2-1**: 최종 배포 링크 생성 (Streamlit Community Cloud 등)
- [ ] **Task 4-2-2**: 포트폴리오용 데모 시연 영상 또는 스크린샷 확보
