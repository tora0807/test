import streamlit as st

# 初期化：セッションステートに現在の問題番号を保持
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# 問題データ（ここでは例として3問。100問まで追加できます）
questions = [
    {
        "question": "糖尿病の三大症状に含まれないものはどれ？",
        "options": ["多尿", "多飲", "頻脈", "多食"],
        "answer": "頻脈",
        "explanation": "糖尿病の三大症状は「多尿・多飲・多食」。頻脈は含まれません。"
    },
    {
        "question": "高血圧の診断基準は収縮期血圧が何mmHg以上？",
        "options": ["120", "130", "140", "150"],
        "answ
