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

# セッション状態の初期化
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# 現在の問題
q = questions[st.session_state.question_index]

# 問題表示
st.write(f"### 問題 {st.session_state.question_index + 1}")
st.write(q["question"])

# 選択肢の表示と選択結果取得
selected = st.radio("選択肢を選んでください：", q["options"], index=None)

# 解答の自動表示（選んだら即反映）
if selected:
    st.write(f"📝 あなたの選択：**{selected}**")
    st.write(f"✅ 正解：**{q['answer']}**")

    if selected == q["answer"]:
        st.success("正解です！🎉")
    else:
        st.error("不正解です。復習しましょう。")

    # 次の問題に進む
    if st.button("次の問題へ"):
        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1
        else:
            st.info("全ての問題が終了しました。お疲れさまでした！")
