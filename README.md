import streamlit as st

# セッション状態の初期化
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

# 問題表示
st.write(f"問題 {st.session_state.current_question + 1}")

# 解答が選択されていない場合のみ選択肢を表示
if not st.session_state.answered:
    answer = st.radio("選択してください", ["選択肢1", "選択肢2", "選択肢3"])
    
    if st.button("解答"):
        st.session_state.answered = True
        # 解答の処理
        st.write(f"あなたの解答: {answer}")

# 次の問題ボタンは解答後のみ表示
if st.session_state.answered:
    if st.button("次の問題"):
        st.session_state.current_question += 1
        st.session_state.answered = False
        st.rerun()