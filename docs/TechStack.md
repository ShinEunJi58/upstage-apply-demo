# Tech Stack Document
## NSR Smart Navigator (북극항로 수출 전략 에이전트)

| 항목 | 내용 |
| --- | --- |
| **프로젝트명** | NSR Smart Navigator |
| **문서 작성일** | 2024-12-22 |

---

## 1. Core Engine (AI Platform)
### **POPOW.ai (AI Agent Builder)**
*   **Role**: 전체 에이전트의 구축, 배포, 대화 흐름 관리 (Orchestration).
*   **Selection Reason**: 
    *   No-code/Low-code 환경으로 빠른 프로토타이핑 및 배포 가능.
    *   Knowledge Base 연동 및 Web Browsing 플러그인 등 확장성 용이.
    *   대화형 인터페이스(Chat UI) 기본 제공.

## 2. Knowledge Base (RAG Data)
에이전트가 답변 생성 시 참조할 핵심 내부 데이터입니다.

### **2.1. 정형 데이터 (Structured Data)**
*   **운임 및 소요 시간 데이터 (Excel/CSV)**
    *   **내용**: 부산-함부르크 기준 수에즈 운하 vs 북극항로 비교 데이터.
    *   **Fields**: `Route_Type` (NSR/Suez), `Total_Distance` (km), `Lead_Time` (days), `Fuel_Cost_Index`, `Container_Cost`.

### **2.2. 비정형 데이터 (Unstructured Data)**
*   **유망 품목 가이드 (PDF/Markdown)**
    *   **내용**: K-Food, K-Beauty 등 유럽 수출 유망 품목 리스트 및 특성.
    *   **활용**: 사용자 질문(품목 추천 등)에 대한 Context 제공.
*   **HS Code 매핑 테이블**
    *   **내용**: 주요 수출 품목별 HS Code 및 관세 정보 팁.

## 3. External Integrations (Tools)
외부 정보를 실시간으로 가져오기 위한 도구입니다.

### **3.1. Web Browsing Plugin**
*   **Purpose**: 실시간 리스크 및 현황 모니터링.
*   **Trigger Keywords**: "안전해?", "리스크", "뉴스", "해빙", "운항 여부".
*   **Sources**:
    *   글로벌 해운 뉴스 (Bloomberg Shipping, Tradewinds 등)
    *   러시아-우크라이나 관련 지정학적 뉴스 소스
    *   북극 해빙 농도 리포트 (NSIDC 등 공개 데이터)

## 4. System Architecture (Workflow)
```mermaid
graph TD
    User[User (Buyer/Logistics Mgr)] -->|Question| Agent[POPOW Agent]
    
    subgraph "Reasoning Engine"
        Agent -->|Intent Analysis| Classifier{Intent Classifier}
    end
    
    Classifier -->|Cost/Route| KB_Calc[(Knowledge Base: Cost Data)]
    Classifier -->|Item Recommendation| KB_Item[(Knowledge Base: Product Guide)]
    Classifier -->|Risk/News| Web[Web Browsing Plugin]
    
    KB_Calc -->|Retrieved Context| LLM[LLM Generation]
    KB_Item -->|Retrieved Context| LLM
    Web -->|Real-time Info| LLM
    
    LLM -->|Final Answer| Agent
    Agent -->|Response| User
```

## 5. Development Environment
*   **OS**: Windows/Mac (Web-based Builder)
*   **Browser**: Chrome (Recommended for POPOW editing)
*   **Documentation**: Markdown (PRD, Ideation), Mermaid (Diagrams)
