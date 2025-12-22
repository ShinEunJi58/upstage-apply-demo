# Project Task List
## NSR Smart Navigator Project

| 항목 | 내용 |
| --- | --- |
| **프로젝트명** | NSR Smart Navigator |
| **문서 목적** | 프로젝트 진행 단계별 세부 작업 관리 |
| **작성일** | 2024-12-22 |

---

## Phase 1: Planning & Design (기획 및 설계)
> 프로젝트의 방향성을 설정하고 필요한 요구사항과 기술 스택을 정의합니다.

### Epic 1-1: Requirement Analysis (요구사항 분석)
- [x] **Task 1-1-1**: `docs/ideation.md` 분석 및 핵심 기능 도출
- [x] **Task 1-1-2**: `docs/PRD.md` 작성 (핵심 기능, 타겟 유저, 페르소나 정의)
- [x] **Task 1-1-3**: `docs/TechStack.md` 작성 (구현 도구, 데이터 구조 정의)

### Epic 1-2: Data Schema Design (데이터 설계)
- [ ] **Task 1-2-1**: 운임 비교용 정형 데이터(Excel) 스키마 정의 (`Route`, `Distance`, `Cost`, `Time` 등)
- [ ] **Task 1-2-2**: 품목 추천용 비정형 데이터(Markdown/PDF) 구조 설계
- [ ] **Task 1-2-3**: 시스템 프롬프트(System Prompt) 초안 작성 (페르소나 설정)

---

## Phase 2: Data Preparation (데이터 준비)
> 에이전트가 학습할 Knowledge Base 데이터를 실제 파일로 제작합니다.

### Epic 2-1: Structured Data Construction (정형 데이터 구축)
- [ ] **Task 2-1-1**: 가상의 부산-함부르크 운임 비교 데이터 생성 (Dummy Data or Researched Data)
- [ ] **Task 2-1-2**: CSV/Excel 파일로 저장 및 데이터 정합성 검토

### Epic 2-2: Unstructured Data Construction (비정형 데이터 구축)
- [ ] **Task 2-2-1**: 유럽 수출 유망 품목(K-Food, K-Beauty 등) 리스트 정리
- [ ] **Task 2-2-2**: 품목별 HS Code 및 관세 팁 자료 수집 및 문서화

---

## Phase 3: Agent Implementation (에이전트 구현)
> POPOW.ai를 활용하여 실제로 작동하는 에이전트를 구축합니다.

### Epic 3-1: Agent Setup (기본 설정)
- [ ] **Task 3-1-1**: POPOW 프로젝트 생성 및 기본 페르소나(System Prompt) 입력
- [ ] **Task 3-1-2**: Knowledge Base(RAG) 파일 업로드 및 인덱싱

### Epic 3-2: Skill & Tool Integration (기능 연동)
- [ ] **Task 3-2-1**: Web Browsing 플러그인 연동 설정
- [ ] **Task 3-2-2**: 사용자 의도(Intent)별 답변 로직 테스트 (운임 계산 vs 뉴스 검색 분기 처리)

---

## Phase 4: Verification & Deployment (검증 및 배포)
> 구현된 에이전트를 테스트하고 최종 산출물로 배포합니다.

### Epic 4-1: Testing (테스트)
- [ ] **Task 4-1-1**: 시나리오 테스트 (운임 문의, 리스크 문의, 추천 문의)
- [ ] **Task 4-1-2**: 답변 정확도 검증 및 Hallucination 점검
- [ ] **Task 4-1-3**: 프롬프트 최적화 (튜닝)

### Epic 4-2: Launch (배포)
- [ ] **Task 4-2-1**: 최종 배포 링크 생성
- [ ] **Task 4-2-2**: 포트폴리오용 데모 시연 영상 또는 스크린샷 확보
