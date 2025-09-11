import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# セッションステート初期化
if 'q_num' not in st.session_state:
    st.session_state.q_num = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# ダミーの問題リスト（実際は医学問題を入れてください）
questions = [
    "問題1: ○○とは何か？",
    "問題2: △△の症状は？",
    # ... 10問分
] * 1  # 10問分

def show_question(q_num):
    st.write(questions[q_num])
    answer = st.text_input("回答を入力してください", key=f"answer_{q_num}")
    if st.button("次へ", key=f"next_{q_num}"):
        st.session_state.answers.append(answer)
        st.session_state.q_num += 1
        st.experimental_rerun()

def show_forgetting_curve():
    st.write("忘却曲線のグラフ")

    # 時間（単位は時間など）
    t = np.linspace(0, 24, 100)
    # 忘却曲線のモデル例（指数関数的に記憶が減る）
    retention = np.exp(-0.1 * t)

    fig, ax = plt.subplots()
    ax.plot(t, retention)
    ax.set_xlabel('時間（時間）')
    ax.set_ylabel('記憶率')
    ax.set_title('忘却曲線')
    st.pyplot(fig)

if st.session_state.q_num < 10:
    show_question(st.session_state.q_num)
else:
    show_forgetting_curve()
