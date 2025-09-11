import streamlit as st
import numpy as np
import pandas as pd

# --- 問題例（50問） ---
questions = [f"問題{i+1}: 医学知識に関する質問をここに書く" for i in range(50)]

# --- セッションステート初期化 ---
if 'q_num' not in st.session_state:
    st.session_state.q_num = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# --- クイズ画面表示関数 ---
def show_question(q_num):
    st.subheader(f"第 {q_num + 1} 問")
    st.write(questions[q_num])
    answer = st.text_input("回答を入力してください", key=f"answer_{q_num}")
    if st.button("次へ", key=f"next_{q_num}"):
        if not answer.strip():
            st.warning("回答を入力してください。")
            return
        st.session_state.answers.append(answer)
        st.session_state.q_num += 1
        st.experimental_rerun()

# --- 忘却曲線表示関数 ---
def show_forgetting_curve():
    st.success("50問解き終わりました！お疲れ様です🎉")
    st.subheader("📉 忘却曲線グラフ")

    t = np.linspace(0, 72, 100)  # 0〜72時間（3日間）
    retention = np.exp(-0.05 * t)  # 忘却曲線モデル（指数関数）

    df = pd.DataFrame({
        '時間（h）': t,
        '記憶率': retention
    })

    st.line_chart(df.rename(columns={'時間（h）': 'index'}).set_index('index'))

    st.markdown("""
    - 時間の経過とともに記憶が薄れることを示すグラフです。
    - 定期的な復習で記憶を定着させましょう。
    """)

# --- メイン処理 ---
st.title("🩺 医学知識クイズアプリ")

if st.session_state.q_num < len(questions):
    show_question(st.session_state.q_num)
else:
    show_forgetting_curve()
