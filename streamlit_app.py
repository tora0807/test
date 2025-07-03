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
user_name = st.text_input("あなたの名前を教えてください:")

if user_name:
    st.write(f"こんにちは、{user_name}さん！クイズを始めましょう！")

    try:
        questions = load_questions_from_excel("問題集.xlsx")
    except Exception as e:
        st.error(f"問題の読み込みに失敗しました: {e}")
        st.stop()

    # セッションステートの初期化
    if "question_index" not in st.session_state:
        st.session_state.question_index = random.randint(0, len(questions) - 1)
        st.session_state.answered = False
        st.session_state.selected_option = None

    # 現在の問題
    current_question = questions[st.session_state.question_index]

    # 問題文表示
    st.subheader(current_question["question"])

    # 選択肢表示（常に同じkeyを使用）
    selected = st.radio(
        "選んでください:",
        current_question["options"],
        index=0,
        key="radio_choice",
        disabled=st.session_state.answered  # 回答後は無効
    )

    # 回答前のボタン表示
    if not st.session_state.answered:
        if st.button("回答"):
            st.session_state.selected_option = selected
            st.session_state.answered = True
            st.experimental_rerun()  # 状態更新後に再レンダリング

    # 回答後のフィードバック
    if st.session_state.answered:
        if st.session_state.selected_option == current_question["answer"]:
            st.success("正解です！🎉")
        else:
            st.error(f"残念！正解は「{current_question['answer']}」です。")

        if st.button("次の問題へ"):
            st.session_state.question_index = random.randint(0, len(questions) - 1)
            st.session_state.answered = False
            st.session_state.selected_option = None
            st.experimental_rerun()
else:
    st.write("名前を入力して、クイズを開始してください！")
