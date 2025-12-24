import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="NSR Smart Navigator",
    page_icon="🚢",
    layout="wide"
)

# Custom CSS for aesthetic improvements
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🚢 NSR Smart Navigator")
    st.info("북극항로 수출 전략 AI 에이전트")
    
    menu = st.radio(
        "메뉴 선택",
        ["Home", "💰 경제성 진단 (Cost Calculator)", "⚠️ 리스크 모니터링 (Risk Radar)", "📦 유망 품목 추천 (Item Matcher)"]
    )
    
    st.markdown("---")
    st.caption("Developed by Upstage Apply Demo Team")

# Main Content
if menu == "Home":
    st.title("⚓ 북극항로 수출 전략 에이전트")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Welcome to NSR Smart Navigator
        
        **NSR Smart Navigator**는 복잡한 북극항로(NSR: Northern Sea Route) 물류 데이터를 AI 에이전트가 실시간으로 분석하여, 
        유럽 수출을 희망하는 중소기업에게 최적의 물류 경로와 리스크 정보를 제공하는 서비스입니다.
        
        #### 🚀 주요 기능
        - **💰 경제성 진단**: 기존 수에즈 운하 항로 대비 거리, 소요 시간, 비용 절감 효과를 분석합니다.
        - **⚠️ 리스크 모니터링**: 해빙 농도 및 지정학적 리스크를 실시간으로 모니터링합니다.
        - **📦 유망 품목 추천**: 빠른 배송이 필요한 최적의 수출 품목을 제안합니다.
        """)
        
    with col2:
        st.image("https://images.unsplash.com/photo-1541457816826-64197e42d746?auto=format&fit=crop&q=80&w=2070", caption="Northern Sea Route")

    st.markdown("---")
    st.info("👈 왼쪽 사이드바 메뉴를 통해 각 기능을 체험해보세요.")

elif menu == "💰 경제성 진단 (Cost Calculator)":
    st.title("💰 북극항로 경제성 진단")
    st.caption("기존 수에즈 운하 항로와 북극항로(NSR)의 경제성을 비교 분석합니다.")
    
    # Load Data
    try:
        df = pd.read_csv("data/route_data_sample.csv")
        
        # User Input
        with st.container():
            st.subheader("📋 화물 정보 입력")
            col_input1, col_input2 = st.columns(2)
            with col_input1:
                containers = st.number_input("화물 컨테이너 수 (TEU)", min_value=1, value=10)
            with col_input2:
                # Add dummy destination selection for UX
                destination = st.selectbox("목적지 (유럽)", ["Rotterdam (Netherlands)", "Hamburg (Germany)", "Southampton (UK)"])
        
        # Calculate Costs
        df['Total_Cost'] = df['Container_Cost'] * containers
        
        nsr_data = df[df['Route'] == 'NSR'].iloc[0]
        suez_data = df[df['Route'] == 'Suez'].iloc[0]
        
        # Summary Metrics
        st.markdown("### 📊 분석 결과")
        m1, m2, m3 = st.columns(3)
        
        cost_saving = suez_data['Total_Cost'] - nsr_data['Total_Cost']
        time_saving = suez_data['Lead_Time'] - nsr_data['Lead_Time']
        dist_saving = suez_data['Distance'] - nsr_data['Distance']
        
        with m1:
            st.metric("예상 절감 비용", f"${cost_saving:,.0f}", delta=f"Vs Suez")
        with m2:
            st.metric("단축 소요 시간", f"{time_saving} Days", delta=f"Vs Suez")
        with m3:
            st.metric("단축 운항 거리", f"{dist_saving:,.0f} km", delta=f"Vs Suez")
            
        # Visualizations
        st.markdown("### 📈 상세 비교")
        tab1, tab2 = st.tabs(["비용/거리 비교", "소요 시간 비교"])
        
        with tab1:
            fig_cost = px.bar(df, x='Route', y='Total_Cost', title=f"총 물류비용 비교 ({containers} TEU 기준)", 
                             color='Route', text='Total_Cost', color_discrete_map={'NSR': '#1f77b4', 'Suez': '#ff7f0e'})
            fig_cost.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
            st.plotly_chart(fig_cost, use_container_width=True)
            
        with tab2:
            fig_time = px.bar(df, x='Route', y='Lead_Time', title="운항 소요 시간 (Lead Time) 비교",
                             color='Route', text='Lead_Time', color_discrete_map={'NSR': '#1f77b4', 'Suez': '#ff7f0e'})
            fig_time.update_traces(texttemplate='%{text} Days', textposition='outside')
            st.plotly_chart(fig_time, use_container_width=True)
            
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류가 발생했습니다: {e}")
        st.write("data/route_data_sample.csv 파일을 확인해주세요.")

elif menu == "⚠️ 리스크 모니터링 (Risk Radar)":
    st.title("⚠️ 리스크 모니터링")
    st.caption("북극항로 운항에 영향을 미치는 주요 리스크 요인을 실시간으로 모니터링합니다.")
    
    col_risk1, col_risk2 = st.columns(2)
    
    with col_risk1:
        st.subheader("🧊 해빙 농도 (Sea Ice)")
        # Mock Metric
        conc = 45 # Mock percent
        st.metric(label="현재 해빙 농도", value=f"{conc}%", delta="-5% (전주 대비 감소)")
        st.progress(conc/100)
        if conc < 50:
            st.success("✅ 운항 가능 (해빙 농도 양호)")
        else:
            st.warning("⚠️ 주의 필요 (쇄빙선 필수)")
            
    with col_risk2:
        st.subheader("🌍 지정학적 리스크")
        # Mock Status
        risk_level = "주의 (Caution)"
        st.metric(label="현재 리스크 레벨", value=risk_level, delta_color="inverse")
        st.warning("일부 구간 통항 제한 가능성 있음 (러시아 영해)")
    
    st.markdown("### 📡 실시간 뉴스 모니터링")
    st.markdown("""
    - [News] 북극항로 해빙 속도, 예년보다 1.5배 빨라... 물류망 청신호? (2025.12.20)
    - [Alert] 러시아-유럽 지정학적 긴장 고조, 보험료율 변동 주의 (2025.12.22)
    - [Market] 주요 해운사, 2026년 NSR 시범 운항 확대 계획 발표 (2025.12.23)
    """)

elif menu == "📦 유망 품목 추천 (Item Matcher)":
    st.title("📦 수출 유망 품목 추천")
    st.caption("납기 민감도와 물류 비용을 고려하여 북극항로 이용 시 이점이 큰 품목을 추천합니다.")
    
    with st.form("recommendation_form"):
        st.write("#### 귀사의 비즈니스 상황을 선택해주세요")
        
        industry = st.selectbox("산업군", ["제조업 (일반)", "식품/바이오", "패션/의류", "정밀기기/전자"])
        urgency = st.slider("납기 민감도 (1: 낮음 ~ 5: 매우 높음)", 1, 5, 3)
        volume = st.radio("예상 물동량", ["소량 (LCL)", "대량 (FCL)"])
        
        submitted = st.form_submit_button("추천 품목 확인")
        
    if submitted:
        st.divider()
        st.subheader("🎯 AI 추천 결과")
        
        if urgency >= 4 or industry in ["식품/바이오", "패션/의류"]:
            recommendation = "강력 추천"
            reason = "북극항로는 수에즈 운하 대비 운송 시간을 획기적으로 단축(약 10~15일)할 수 있어, 신선도가 생명인 식품이나 트렌드 변화가 빠른 패션 의류, 재고 관리 비용이 높은 정밀 부품 수출에 매우 적합합니다."
            items = ["🍓 신선 딸기/과일", "👗 패스트 패션 의류", "📱 최신 전자부품"]
            color = "green"
        elif urgency == 3:
            recommendation = "검토 필요"
            reason = "비용 절감 효과와 시간 단축 효과를 종합적으로 고려해야 합니다. 계절적 요인에 따라 유동적으로 선택하는 것이 좋습니다."
            items = ["🚗 자동차 부품", "⚙️ 일반 기계류", "🧴 화장품"]
            color = "orange"
        else:
            recommendation = "추천하지 않음"
            reason = "납기에 여유가 있다면 비용 효율성이 더 좋은 기존 항로(수에즈)가 유리할 수 있습니다."
            items = ["🪵 원자재", "🏗️ 대형 구조물"]
            color = "red"
            
        st.markdown(f":{color}[### {recommendation}]")
        st.write(reason)
        
        if items:
            st.write("#### 💡 추천 품목 리스트")
            cols = st.columns(len(items))
            for idx, item in enumerate(items):
                with cols[idx]:
                    st.success(item)
