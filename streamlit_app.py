import streamlit as st
import random

st.title("🧠 医学知識クイズアプリ")
st.markdown("各セット10問。4択クイズにチャレンジ！")

# --- 100問を10セットに分けたサンプル問題（簡易版） ---
quiz_data = []

for set_num in range(1, 11):
    for i in range(1, 11):
        q_num = (set_num - 1) * 10 + i
        quiz_data.append({
            "set": set_num,
            "difficulty": random.choice(["easy", "medium", "hard"]),
            "question": f"問題 {q_num}: 医学に関する質問です（セット{set_num}）",
            "options": [f"選択肢A-{q_num}", f"選択肢B-{q_num}", f"選択肢C-{q_num}", f"選択肢D-{q_num}"],
            "answer": f"選択肢{random.choice(['A', 'B', 'C', 'D'])}-{q_num}"
        })

set_numbers = sorted(set(q["set"] for q in quiz_data))
selected_set = st.selectbox("クイズセットを選んでください", set_numbers)

# --- セット変更時の初期化 ---
if "prev_set" not in st.session_state or st.session_state.prev_set != selected_set:
    # 選んだセットの問題だけを抽出
    filtered_questions = [q for q in quiz_data if q["set"] == selected_set]
    
    # 問題リストをシャッフルして順番を固定
    random.seed(42)
    random.shuffle(filtered_questions)
    
    # シャッフル済み問題リストをセッションに保存
    st.session_state.questions = filtered_questions
    
    # 問題番号、スコア、回答状態をリセット
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    
    st.session_state.prev_set = selected_set

questions = st.session_state.questions

# --- 現在の問題を取得 ---
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]

    st.markdown(f"### Q{st.session_state.current_q + 1}: {q['question']}")
    st.mark
