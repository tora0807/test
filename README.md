import streamlit as st

# 初期化
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# ボタンを押したら状態を変更
if st.button("解答を表示"):
    st.session_state.show_answer = True

# 状態が True なら答えを表示
if st.session_state.show_answer:
    st.write("正解は A です")
