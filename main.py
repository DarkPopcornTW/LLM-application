import streamlit as st
from utils import generate_ig


st.header("爆款IG AI寫作助手 ✏️")
with st.sidebar:
    openai_api_key = st.text_input("請輸入OpenAI API金鑰：", type="password")
    st.markdown("[取得OpenAI API金鑰](https://platform.openai.com/account/api-keys)")

theme = st.text_input("主題")
submit = st.button("開始寫作")

if submit and not openai_api_key:
    st.info("請輸入你的OpenAI API金鑰")
    st.stop()
if submit and not theme:
    st.info("請輸入生成內容的主題")
    st.stop()
if submit:
    with st.spinner("AI正在努力創作中，請稍等..."):
        result = generate_ig(theme, openai_api_key)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown("##### ig標題1")
        st.write(result.titles[0])
        st.markdown("##### ig標題2")
        st.write(result.titles[1])
        st.markdown("##### ig標題3")
        st.write(result.titles[2])
        st.markdown("##### ig標題4")
        st.write(result.titles[3])
        st.markdown("##### ig標題5")
        st.write(result.titles[4])
    with right_column:
        st.markdown("##### ig正文")
        st.write(result.content)
