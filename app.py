import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="NSR Smart Navigator",
    page_icon="🚢",
    layout="wide"
)

# Sidebar
st.sidebar.title("🚢 NSR Smart Navigator")
st.sidebar.info("북극항로 수출 전략 AI 에이전트")

menu = st.sidebar.radio(
    "메뉴 선택",
    ["Home", "💰 경제성 진단 (Cost Calculator)", "⚠️ 리스크 모니터링 (Risk Radar)", "📦 유망 품목 추천 (Item Matcher)"]
)

# Main Content
if menu == "Home":
    st.title("⚓ 북극항로 수출 전략 에이전트")
    st.markdown("""
    ### Welcome to NSR Smart Navigator
    
    복잡한 북극항로(NSR) 물류 데이터를 AI가 분석하여 최적의 솔루션을 제공합니다.
    
    **핵심 기능:**
    - **경제성 진단**: 수에즈 운하 대비 거리/비용 절감 효과 분석
    - **리스크 모니터링**: 해빙 농도 및 지정학적 리스크 실시간 확인
    - **유망 품목 추천**: 빠른 배송이 필요한 최적 수출 품목 제안
    """)
    
    st.image("https://images.unsplash.com/photo-1541457816826-64197e42d746?auto=format&fit=crop&q=80&w=2070", caption="Northern Sea Route")

elif menu == "💰 경제성 진단 (Cost Calculator)":
    st.title("💰 북극항로 경제성 진단")
    st.write("수에즈 운하 vs 북극항로 비교 분석 기능을 제공할 예정입니다.")
    
elif menu == "⚠️ 리스크 모니터링 (Risk Radar)":
    st.title("⚠️ 리스크 모니터링")
    st.write("해빙 농도 및 지정학적 리스크 신호등 기능을 제공할 예정입니다.")

elif menu == "📦 유망 품목 추천 (Item Matcher)":
    st.title("📦 수출 유망 품목 추천")
    st.write("사용자 상황에 맞는 최적의 수출 품목 추천 기능을 제공할 예정입니다.")
