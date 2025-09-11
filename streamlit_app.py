import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# セッションステートの初期化
if 'q_num' not in st.session_state:
    st.session_state.q_num = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

questions = [
    "問題1: ○○とは何か？",
    "問題2: △△の症状は？",
    "問題3: ××の治療法は？",
    "問題4: △△の検査法は？",
    "問題5: ○○の副作用は？",
    "問題6: ××の予防法は？",
    "問題7: △△の診断基準は？",
    "問題8: ○○の病態生理は？",
    "問題9: ××の合併症は？",
    "問題10: △△の疫学は？",
]

def show_question(q_num):
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
    st
