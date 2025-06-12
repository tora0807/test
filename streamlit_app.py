import streamlit as st

st.title("🩺 医学クイズアプリ")

# クイズデータ（問題・選択肢・答え）
questions = [
    {
        "question": "風邪の原因になるのは？",
        "options": ["ウイルス", "細菌", "カビ", "花粉"],
        "answer": "ウイルス"
    },
    {
        "question": "人の体で一番大きな臓器は？",
        "options": ["肝臓", "皮膚", "肺", "腸"],
        "answer": "皮膚"
    },
    {
        "question": "鼻血が出たときの正しい対処は？",
        "options": ["上を向く", "仰向けで寝る", "小鼻をつまんで前かがみ", "ティッシュを詰める"],
        "answer": "小鼻をつまんで前かがみ"
    }
]

score = 0

for idx, q in enumerate(questions):
    st.subheader(f"Q{idx+1}: {q['question']}")
    user_answer = st.radio("選択肢：", q["options"], key=f"q{idx}")
    if user_answer:
        if user_answer == q["answer"]:
            st.success("正解！🎉")
            score += 1
        else:
            st.error(f"不正解 ❌ 正解は「{q['answer']}」でした。")

st.markdown("---")
st.subheader(f"✅ あなたの得点：{score} / {len(questions)}")
