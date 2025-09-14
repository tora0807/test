import streamlit as st
import random

st.title("🧠 医学知識クイズアプリ")
st.markdown("各セット10問。4択クイズにチャレンジ！")

# --- 100問を10セットに分けたサンプル問題（簡易版） ---
quiz_data = []

# 1セット目〜10セット目のダミー問題作成
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

# セット番号のリストを作成
set_numbers = sorted(set(q["set"] for q in quiz_data))
selected_set = st.selectbox("クイズセットを選んでください", set_numbers)

# セット変更時に状態をリセット
if "prev_set" not in st.session_state:
    st.session_state.prev_set = selected_set
elif st.session_state.prev_set != selected_set:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.prev_set = selected_set

# 選んだセットの問題をフィルタリング
questions = [q for q in quiz_data if q["set"] == selected_set]
random.seed(42)  # 順序を固定
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

# 現在の問題番号が範囲内なら
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    
    st.markdown(f"### Q{st.session_state.current_q + 1}: {q['question']}")
    st.markdown(f"難易度: **{q['difficulty'].capitalize()}**")

    # 選択肢をシャッフルして表示
    options = q["options"].copy()
    random.shuffle(options)

    st.session_state.selected_option = st.radio(
        "選択肢を選んでください：",
        options,
        index=0,
        key=f"option_{st.session_state.current_q}"
    )

    # 回答するボタン
    if not st.session_state.answered:
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

    # 次の問題へボタン（回答後のみ表示）
    if st.session_state.answered:
        if st.button("次の問題へ", key=f"next_btn_{st.session_state.current_q}"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.selected_option = None
            st.experimental_rerun()

# クイズ終了時
else:
    st.markdown("## ✅ クイズ終了！")
    st.success(f"あなたの得点は **{st.session_state.score} / {len(questions)} 点** です")
    if st.button("最初からやり直す"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected_option = None
        st.experimental_rerun()
