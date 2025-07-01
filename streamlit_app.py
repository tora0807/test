import streamlit as st
import random

# クイズのデータ (質問と選択肢、正解)
questions = [
    {
        "question": "人間の心臓は1日に何回鼓動するか?",
        "options": ["10,000回", "50,000回", "100,000回", "200,000回"],
        "answer": "100,000回"
    },
    {
        "question": "赤血球の寿命は約何日か?",
        "options": ["30日", "60日", "90日", "120日"],
        "answer": "120日"
    },
    {
        "question": "人間の体内で最大の臓器は何か?",
        "options": ["肝臓", "腎臓", "皮膚", "脳"],
        "answer": "皮膚"
    },
    {
        "question": "人間の骨の数は成人で何本か?",
        "options": ["206本", "250本", "300本", "400本"],
        "answer": "206本"
    },
]

# アプリのタイトル
st.title('医学クイズアプリ')

# ユーザー名を入力してもらう
user_name = st.text_input("あなたの名前を教えてください:")

if user_name:
    st.write(f"こんにちは、{user_name}さん！クイズを始めましょう！")

    # クイズの問題をランダムにシャッフル
    question = random.choice(questions)

    # 問題を表示
    st.subheader(question['question'])

    # ラジオボタンで選択肢を表示
    answer = st.radio(
        "選んでください:",
        question['options']
    )

    # 回答ボタンを作成
    if st.button("回答"):
        if answer == question['answer']:
            st.success("正解です！🎉")
        else:
            st.error(f"残念！正解は「{question['answer']}」です。")
else:
    st.write("名前を入力して、クイズを開始してください！")

