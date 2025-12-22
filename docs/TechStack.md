# Tech Stack Document
## NSR Smart Navigator (북극항로 수출 전략 에이전트)

| 항목 | 내용 |
| --- | --- |
| **프로젝트명** | NSR Smart Navigator |
| **문서 작성일** | 2024-12-22 |
| **기반 문서** | [PRD](./PRD.md) |

---

## 1. Core Engine (Web Framework)
### **Python (Streamlit)**
*   **Role**: 웹 애플리케이션 프론트엔드 및 백엔드 로직 구현.
*   **Selection Reason**: 
    *   **Rapid Development**: 파이썬 코드로 빠르게 데이터 애플리케이션 구축 가능.
    *   **Flexibility**: LangChain 등 최신 LLM 라이브러리와의 자유로운 연동.
    *   **Interactive**: 채팅 인터페이스(`st.chat_message`) 및 데이터 시각화 도구 기본 내장.

## 2. Knowledge Base (RAG Data)
에이전트가 답변 생성 시 참조할 핵심 내부 데이터입니다. **할루시네이션(거짓 답변) 방지**를 위해 신뢰할 수 있는 데이터를 구축합니다.

### **2.1. 정형 데이터 (Structured Data)**
*   **운임 및 소요 시간 데이터 (Excel/CSV)**
    *   **용도**: '북극항로 경제성 진단' 기능 구현.
    *   **Schema**:
        | Field Name | Type | Description |
        | --- | --- | --- |
        | `Route_Type` | String | 'NSR'(북극항로) 또는 'Suez'(수에즈) |
        | `Origin` | String | 출발지 (예: Busan) |
        | `Destination` | String | 도착지 (예: Hamburg) |
        | `Distance_km` | Number | 총 운항 거리 |
        | `Lead_Time_days` | Number | 예상 소요 일수 |
        | `Cost_Index` | Number | 운임 지수 (비교용) |

### **2.2. 비정형 데이터 (Unstructured Data)**
*   **유망 품목 가이드 (PDF/Markdown)**
    *   **용도**: '수출 유망 품목 추천' 기능 구현.
    *   **내용**: K-Food, K-Beauty, 패스트패션 등 카테고리별 유럽 시장 트렌드 및 추천 사유.
*   **HS Code 매핑 테이블**
    *   **내용**: 주요 품목별 HS Code 및 EU 관세 정보.

## 3. External Integrations (Tools)
외부 정보를 실시간으로 가져오기 위한 도구입니다.

### **3.1. Web Browsing Plugin**
*   **Purpose**: '지정학적 리스크 모니터링' 기능 구현 (실시간성 확보).
*   **Trigger Keywords**: "안전해?", "해빙", "뉴스", "러시아", "운항 여부".
*   **Target Sources**:
    *   NSIDC (National Snow and Ice Data Center) - 해빙 정보
    *   Global Shipping News - 물류/해운 뉴스
    *   Mainstream News - 지정학적 이슈

## 4. System Architecture
```mermaid
graph TD
    User[사용자 (수출기업)] -->|질문 입력| App[Streamlit App]
    
    subgraph "Reasoning & Retrieval"
        App -->|의도 파악| Router{Intent Router}
        Router -->|비용/시간 문의| KB_Cost[(KB: 운임 데이터)]
        Router -->|품목 추천| KB_Item[(KB: 유망 품목)]
        Router -->|리스크/뉴스| Web[Web Browsing Tool]
    end
    
    KB_Cost -->|Context| LLM
    KB_Item -->|Context| LLM
    Web -->|Real-time Info| LLM
    
    LLM -->|최적 답변 생성| App
    App -->|답변 출력| User
```

## 5. Development Environment
*   **Language**: Python 3.10+
*   **Framework**: Streamlit
*   **Libraries**: LangChain, OpenAI (or Upstage Solar), Pandas
*   **Documentation Tools**: Markdown (기획서), Mermaid (다이어그램).
