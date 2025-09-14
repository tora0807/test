import streamlit as st
import random

# タイトル
st.title("🧠 医学知識クイズアプリ")
st.markdown("各セット10問。4択クイズにチャレンジ！")

# クイズデータ（例として2問だけ入れています。実際は100問をここに入れてください）
quiz_data = [
    {"set":1, "question":"正常な体温はおおよそ何度ですか？", "options":["35.0℃","36.5℃","37.5℃","38.0℃"], "answer":"36.5℃"},
    {"set":1, "question":"赤血球の主な役割は？", "options":["免疫防御","酸素運搬","ホルモン調整","栄養吸収"], "answer":"酸素運搬"},
    # ← ここに100問分のデータを入れてください（前に作成した問題セット）
]

# セット番号のリストを作成
set_numbers = sorted(set(q["set"] for q in quiz_data))
selected_set = st.selectbox("クイズセットを選んでください", set_numbers)

# 選んだセットの問題をフィルタリング
questions = [q for q in quiz_data if q["set"] == selected_set]
random.seed(42)  # 同じ順序にしたい場合は固定シード
random.shuffle(questions)

# セッションステートの初期化
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None

# クイズ表示（1問ずつ）
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.markdown(f"### Q{st.session_state.current_q + 1}: {q['question']}")
    
    # 選択肢ラジオボタン
    st.session_state.selected_option = st.radio(
        "選択肢を選んでください：",
        q["options"],
        index=None,
        key=f"option_{st.session_state.current_q}"
    )
    
    # 回答ボタン
    if st.button("回答する", key=f"answer_btn_{st.session_state.current_q}"):
        if st.session_state.selected_option:
            if st.session_state.selected_option == q["answer"]:
                st.success("✅ 正解！")
                st.session_state.score += 1
            else:
                st.error(f"❌ 不正解。正解は「{q['answer']}」です。")
            st.session_state.answered = True
        else:
            st.warning("選択肢を選んでください。")

    # 次へ進むボタン（回答後に表示）
    if st.session_state.answered:
        if st.button("次の問題へ", key=f"next_btn_{st.session_state.current_q}"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.experimental_rerun()

# クイズ終了後の表示
else:
    st.markdown("## ✅ クイズ終了！")
    st.success(f"あなたの得点は **{st.session_state.score} / {len(questions)} 点** です")
    if st.button("最初からやり直す"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.experimental_rerun()
