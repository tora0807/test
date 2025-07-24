import streamlit as st

# 医学クイズ（選択肢形式）
questions = [
    {
        "question": "正常な成人の脈拍数は？",
        "options": ["40〜60回/分", "60〜100回/分", "100〜120回/分", "120〜140回/分"],
        "answer": "60〜100回/分"
    },
    {
        "question": "血圧が高い状態を何という？",
        "options": ["低血圧", "正常血圧", "高血圧", "貧血"],
        "answer": "高血圧"
    }
]

# 状態管理
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

# 現在の問題
q = questions[st.session_state.question_index]

# 問題の表示
st.write(f"### 問題 {st.session_state.question_index + 1}")
st.write(q["question"])

# 選択肢の表示（ラジオボタン）
st.session_state.selected_option = st.radio(
    "選択肢を選んでください：",
    q["options"],
    index=0
)

# 解答ボタン
if not st.session_state.answered:
    if st.button("解答する"):
        st.session_state.answered = True

# 解答表示
if st.session_state.answered:
    # ユーザーの選択と正解の表示
    st.write(f"### あなたの選択：{st.session_state.selected_option}")
    st.write(f"### 正解：{q['answer']}")

    # 正誤判定
    if st.session_state.selected_option == q["answer"]:
        st.write("✅ 正解です！")
    else:
        st.write("❌ 不正解です。")

    # 次の問題へ進むボタン
    if st.button("次の問題へ"):
        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1
            st.session_state.answered = False
            st.session_state.selected_option = None
        else:
            st.info("全ての問題が終了しました。お疲れさまでした！")
