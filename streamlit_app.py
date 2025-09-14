import streamlit as st
import random

st.title("🧠 医学知識クイズアプリ")
st.markdown("全100問。10セットに分けて難易度別。4択クイズに挑戦しよう！")

# --- 100問を10セットに分けたサンプル問題 ---
# 実際はここに本物の医学知識問題を入れてください
quiz_data = []
difficulties = ["easy", "medium", "hard"]

for set_num in range(1, 11):
    for i in range(1, 11):
        q_num = (set_num - 1) * 10 + i
        # ランダムに難易度付与（実際は調整してください）
        difficulty = random.choice(difficulties)
        quiz_data.append({
            "set": set_num,
            "difficulty": difficulty,
            "question": f"問題 {q_num}: 医学に関する質問（セット{set_num}, 難易度:{difficulty}）",
            "options": [f"選択肢A-{q_num}", f"選択肢B-{q_num}", f"選択肢C-{q_num}", f"選択肢D-{q_num}"],
            "answer": f"選択肢{random.choice(['A','B','C','D'])}-{q_num}"
        })

# セット選択UI
set_numbers = sorted(set(q["set"] for q in quiz_data))
selected_set = st.selectbox("クイズセットを選んでください", set_numbers)

# セッションステートの初期化
if "prev_set" not in st.session_state or st.session_state.prev_set != selected_set:
    # 選択セットの問題を抽出してシャッフル
    filtered_questions = [q for q in quiz_data if q["set"] == selected_set]
    random.seed(42)  # シード固定で順番固定
    random.shuffle(filtered_questions)

    st.session_state.questions = filtered_questions
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.prev_set = selected_set

questions = st.session_state.questions

# 現在の問題インデックスが範囲内かチェック
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]

    st.markdown(f"### Q{st.session_state.current_q + 1}: {q['question']}")
    st.markdown(f"難易度: **{q['difficulty'].capitalize()}**")

    # 選択肢は一度シャッフルしてセッションに保存
    key_opts = f"shuffled_options_{st.session_state.current_q}"
    if key_opts not in st.session_state:
        options = q["options"].copy()
        random.shuffle(options)
        st.session_state[key_opts] = options
    else:
        options = st.session_state[key_opts]

    st.session_state.selected_option = st.radio(
        "選択肢を選んでください：",
        options,
        key=f"option_{st.session_state.current_q}"
    )

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

    if st.session_state.answered:
        if st.button("次の問題へ", key=f"next_btn_{st.session_state.current_q}"):
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.selected_option = None
            st.experimental_rerun()

else:
    # クイズ終了画面
    st.markdown("## 🎉 クイズ終了！")
    st.success(f"あなたの得点は **{st.session_state.score} / {len(questions)} 点** です")

    if st.button("別のセットを選ぶ"):
        # セッションリセットはセット変更時に行うのでここではrerunだけ
        st.experimental_rerun()
