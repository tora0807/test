import streamlit as st
import random
import pandas as pd

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

st.title('医学クイズアプリ')

user_name = st.text_input("あなたの名前を教えてください:")

if user_name:
    st.write(f"こんにちは、{user_name}さん！クイズを始めましょう！")

    try:
        questions = load_questions_from_excel("問題集.xlsx")
    except Exception as e:
        st.error(f"問題の読み込みに失敗しました: {e}")
        st.stop()

    # セッションステート初期化
    if "question" not in st.session_state:
        st.session_state.question = random.choice(questions)
        st.session_state.answered = False
        st.session_state.selected_option = None

    if not st.session_state.answered:
        # 回答前は選択肢活性化
        selected = st.radio(
            "選んでください:",
            st.session_state.question['options'],
            index=0,
            key="option_select"
        )
        if st.button("回答"):
            st.session_state.selected_option = selected
            st.session_state.answered = True
            # 強制的に再レンダリングさせるため、状態変化は即反映

    else:
        # 回答後は選択肢非活性＆結果表示
        st.radio(
            "選んでください:",
            st.session_state.question['options'],
            index=st.session_state.question['options'].index(st.session_state.selected_option),
            disabled=True
        )
        if st.session_state.selected_option == st.session_state.question['answer']:
            st.success("正解です！🎉")
        else:
            st.error(f"残念！正解は「{st.session_state.question['answer']}」です。")

        if st.button("次の問題へ"):
            st.session_state.question = random.choice(questions)
            st.session_state.answered = False
            st.session_state.selected_option = None

else:
    st.write("名前を入力して、クイズを開始してください！")
