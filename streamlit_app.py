import streamlit as st
import random
import pandas as pd

# Excelファイルから問題を読み込む関数
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

# アプリのタイトル
st.title('医学クイズアプリ')

# ユーザー名を入力してもらう
user_name = st.text_input("あなたの名前を教えてください:")

if user_name:
    st.write(f"こんにちは、{user_name}さん！クイズを始めましょう！")

    try:
        questions = load_questions_from_excel("問題集.xlsx")
    except Exception as e:
        st.error(f"問題の読み込みに失敗しました: {e}")
        st.stop()

    # 問題をランダムにシャッフルして1問選択
    question = random.choice(questions)

    # 問題を表示
    st.subheader(question['question'])

    # ラジオボタンで選択肢を表示
    answer = st.radio(
        "選んでください:",
        question['options']
    )

    # 回答ボタン
    if st.button("回答"):
        if answer == question['answer']:
            st.success("正解です！🎉")
        else:
            st.error(f"残念！正解は「{question['answer']}」です。")
else:
    st.write("名前を入力して、クイズを開始してください！")
