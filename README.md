import streamlit as st

# ==== 問題データ（100問に拡張可能） ====
excel_questions = [
    {
        "number": 1,
        "question": "Excelでセルに数式を入力するには、何の記号で始めますか？",
        "answer": "=",
        "explanation": "Excelでは、数式を入力する際に必ず「=」で始めます。"
    },
    {
        "number": 2,
        "question": "A1からA10の合計を求める関数は？",
        "answer": "=SUM(A1:A10)",
        "explanation": "SUM関数は指定した範囲の合計を計算する関数です。"
    },
    {
        "number": 3,
        "question": "IF関数の基本構文は？",
        "answer": "=IF(条件, 真の場合, 偽の場合)",
        "explanation": "IF関数は条件によって異なる値を返す関数です。"
    },
    # 必要に応じて以下に追加してください（最大100問）
]

# ==== セッションの初期化 ====
if "q_num" not in st.session_state:
    st.session_state.q_num = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "show_explanation" not in st.session_state:
    st.session_state.show_explanation = False

# ==== 現在の問題 ====
current = excel_questions[st.session_state.q_num]

st.title("📘 Excel 学習問題（1問ずつ出題）")
st.subheader(f"問題 {current['number']} / {len(excel_questions)}")
st.write(current["question"])

# ==== ボタンで答え表示 ====
if st.button("✅ 答えを見る"):
    st.session_state.show_answer = True
if st.session_state.show_answer:
    st.success(f"答え：{current['answer']}")

# ==== ボタンで解説表示 ====
if st.button("📖 解説を見る"):
    st.session_state.show_explanation = True
if st.session_state.show_explanation:
    st.info(f"解説：{current['explanation']}")

# ==== 次の問題へ ====
if st.button("➡️ 次の問題へ"):
    if st.session_state.q_num < len(excel_questions) - 1:
        st.session_state.q_num += 1
        # 表示状態をリセット
        st.session_state.show_answer = False
        st.session_state.show_explanation = False
    else:
        st.success("全ての問題が終了しました！お疲れさまでした。")
