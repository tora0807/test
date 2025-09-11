import streamlit as st
import numpy as np
import pandas as pd

# ダミーの50問問題（実際は医学問題に置き換えてください）
questions = [f"問題{i+1}: 医学の問題文をここに書く" for i in range(50)]

# セッションステート初期化
if 'q_num' not in st.session_state:
    st.session_state.q_num = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

def show_question(q_num):
    st.subheader(f"第 {q_num + 1} 問")
    st.write(questions[q_num])
    answer = st.text_input("回答を入力してください", key=f"answer_{q_num}")
    if st.button("次へ", key=f"next_{q_num}"):
        if answer.strip() == "":
            st.warning("回答を入力してください。")
            return
        st.session_state.answers.append(answer)
        st.session_state.q_num += 1
        st.experimental_rerun()

def show_forgetting_curve():
    st.success("50問解き終わりました！お疲れさまです🎉")
    st.subheader("忘却曲線")

    # 時間（0〜72時間）
    t = np.linspace(0, 72, 100)
    retention = np.exp(-0.05 * t)  # 忘却曲線モデル（例）

    df = pd.DataFrame({
        '時間（時間）': t,
        '記憶率': retention
    })

    # 時間をindexにしてline_chart表示
    st.line_chart(df.rename(columns={'時間（時間）': 'index'}).set_index('index'))

    st.markdown("""
    - 忘却曲線は時間とともに記憶が薄れる様子を示します。
    - 定期的な復習が記憶の定着に効果的です。
    """)

st.title("医学知識クイズアプリ")

if st.session_state.q_num < len(questions):
    show_question(st.session_state.q_num)
else:
    show_forgetting_curve()
