import streamlit as st

st.set_page_config(layout="wide", page_title="智慧旅遊 AI")

# 隱藏 Streamlit 預設的 header、footer、padding
st.markdown("""
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding: 0 !important}
    .block-container {padding: 0 !important; max-width: 100% !important}
    header {display: none !important}
    footer {display: none !important}
</style>
""", unsafe_allow_html=True)

with open("travel_rag_website.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1000, scrolling=True)
