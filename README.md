import streamlit as st
import pandas as pd

# === 問題データ読み込み ===
@st.cache_data
def load_questions():
    return pd.read_excel("問題集.xlsx")

df = load_questions()

# === セッション状態 ===
if "q_num" not in st.session_state:
    st.session_state.q_num = 0
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "answered" not in st.session_state:
    st.session_state.answered = False

# === 現在の問題 ===
if st.session_state.q_num < len(df):
    current = df.iloc[st.session_state.q_num]
    st.title("📘 Excel 学習問題（1問ずつ選択・解説付き）")
    st.subheader(f"問題 {int(current['番号'])} / {len(df)}")
    st.write(current["問題文"])

    # 選択肢をラジオボタンで表示
    choices = ["①", "②", "③", "④"]
    opt
