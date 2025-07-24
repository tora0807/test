import streamlit as st

# 医学クイズのリスト
questions = [
    {"question": "正常な成人の呼吸数は？", "answer": "12〜20回/分"},
    {"question": "低血糖の初期症状は？", "answer": "発汗、手の震え、動悸など"},
    {"question": "心筋梗塞の代表的な症状は？", "answer": "胸痛（圧迫感、締め付けられるような痛み）"}
]

# 初期化（最初だけ実行）
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# 現在の問題
q = questions[st.session_state.question_index]

# 問題表示
st.write(f"### 問題 {st.session_state.question_index + 1}")
st.write(q["question"])

# 解答ボタン
if not st.session_state.show_answer:
    if st.button("解答する"):
        st.session_state.show_answer = True
else:
    # 解答表示
    st.success(f"答え：{q['answer']}")

    # 次の問題へ進む
    if st.button("次の問題へ"):
        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1
            st.session_state.show_answer = False  # 解答表示フラグをリセット
        else:
            st.info("全ての問題が終了しました。お疲れさまでした！")
