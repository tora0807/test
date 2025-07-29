import streamlit as st

# 問題の定義（実際には100問用意）
excel_questions = [
    {"number": 1, "question": "Excelでセルに直接数式を入力するにはどの記号を最初に使いますか？", "answer": "="},
    {"number": 2, "question": "SUM関数を使ってA1からA10の合計を出す式は？", "answer": "=SUM(A1:A10)"},
    {"number": 3, "question": "IF関数の基本構文は？", "answer": "=IF(条件, 真の場合, 偽の場合)"},
    # ... 100問まで追加
]

st.title("Excel 問題集（全100問）")

# セッション状態で現在の問題番号を管理
if 'q_num' not in st.session_state:
    st.session_state.q_num = 0

current_q = excel_questions[st.session_state.q_num]

st.subheader(f"問題 {current_q['number']} / 100")
st.write(current_q['question'])

# 回答表示ボタン
if st.button("答えを見る"):
    st.success(f"答え：{current_q['answer']}")

# 次の問題へ
if st.button("次の問題へ"):
    if st.session_state.q_num < len(excel_questions) - 1:
        st.session_state.q_num += 1
    else:
        st.info("すべての問題が完了しました！")
