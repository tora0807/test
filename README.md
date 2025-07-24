import streamlit as st

# 医学クイズのリスト
questions = [
    {"question": "正常な成人の呼吸数は？", "answer": "12〜20回/分"},
    {"question": "低血糖の初期症状は？", "answer": "発汗、手の震え、動悸など"},
    {"question": "心筋梗塞の代表的な症状は？", "answer": "胸痛（圧迫感、締め付けられるような痛み）"}
]

# セッション状態の初期化
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# 現在の問題
q = questions[st.session_state.question_index]

# 表示：問題番号と内容
st.write(f"### 問題 {st.session_state.question_index + 1}")
st.write(q["question"])

# 回答欄（ユーザー入力）
user_input = st.text_input("あなたの解答を入力してください：", value=st.session_state.user_answer)

# 「解答する」ボタン
if not st.session_state.show_answer:
    if st.button("解答する"):
        st.session_state.user_answer = user_input  # 回答を保存
        st.session_state.show_answer = True
else:
    # 表示：ユーザーの回答と正解
    st.info(f"あなたの回答：{st.session_state.user_answer}")
    st.success(f"正解：{q['answer']}")

    # 「次の問題へ」ボタン
    if st.button("次の問題へ"):
        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1
            st.session_state.show_answer = False
            st.session_state.user_answer = ""  # 入力をリセット
        else:
            st.info("全ての問題が終了しました。お疲れさまでした！")
