import streamlit as st

st.title("🏫 学生に多いけが！医学クイズ🩺")
st.write("正しい応急処置を選んで、知識を身につけよう💡")

# クイズのデータ（問題、選択肢、正解）
questions = [
    {
        "question": "バスケの最中に足首をひねった！まずやるべきことは？",
        "options": ["温めて動かす", "すぐに走る", "冷やして安静にする", "そのまま放置する"],
        "answer": "冷やして安静にする"
    },
    {
        "question": "転んですり傷ができた！最初にするべき応急処置は？",
        "options": ["ばんそうこうを貼る", "水で洗い流す", "ガーゼで隠す", "アルコールでこする"],
        "answer": "水で洗い流す"
    },
    {
        "question": "友達がぶつかって前歯を折ってしまった！その歯はどうすればいい？",
        "options": ["水道水でよく洗って捨てる", "牛乳につけて歯科へ", "乾かして保存する", "そのままポケットに入れる"],
        "answer": "牛乳につけて歯科へ"
    },
    {
        "question": "打撲したところがどんどん腫れてきた！この時の対処法は？",
        "options": ["温めてほぐす", "冷やして安静にする", "揉みほぐす", "包帯できつく巻く"],
        "answer": "冷やして安静にする"
    },
    {
        "question": "体育で転んで手をついた！手首が腫れて痛むときの対処は？",
        "options": ["無理に動かして確認", "湿布を貼って放置", "冷やして固定し病院へ", "包帯でしっかり縛る"],
        "answer": "冷やして固定し病院へ"
    }
]

score = 0

# クイズの実行
for idx, q in enumerate(questions):
    st.subheader(f"Q{idx+1}: {q['question']}")
    answer = st.radio("選んでください：", q["options"], key=idx)
    if st.button(f"答え合わせ → Q{idx+1}", key=f"btn{idx}"):
        if answer == q["answer"]:
            st.success("正解！🎉 よくできました。")
            score += 1
        else:
            st.error(f"不正解❌ 正解は「{q['answer']}」です。")

st.markdown("---")
st.subheader(f"📝 あなたのスコア：{score} / {len(questions)}")

st.caption("※このクイズは教育目的です。実際のけがの際は、医師の判断を仰いでください。")
