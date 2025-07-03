import streamlit as st
import random
import pandas as pd

# Excelからクイズ問題を読み込む
@st.cache_data
def load_questions_from_excel(file_path):
    df = pd.read_excel(file_path)
    questions = []
    for _, row in df.iterrows():
        questions.append({
            "question": row["問題文"],
            "options": [row["①"], row["②"], row["③"], row["④"]],
            "answer": row["正解"]
        })
    return questions

# タイトル
st.title('医学クイズアプリ')

# ユーザー名の入力
user_name = st.text_input("あなたの名前を教えてください
