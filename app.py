import streamlit as st

st.set_page_config(page_title="PTT 鄉民口吻語言模型 — 微調成果展示", layout="wide")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden;}
    [data-testid="stDecoration"] {visibility: hidden;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with open("ptt_finetune_showcase.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=6600, scrolling=True)
