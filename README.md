import streamlit as st

st.set_page_config(page_title="Excel問題フラッシャー", page_icon="📊")

st.title("📊 Excel問題フラッシャー")

# 問題の定義
question = "ExcelでセルA1とB1の合計を求める関数はどれですか？"
options = [
    "=合計(A1+B1)",
    "=SUM(A1,B1)",
    "=TOTAL(A1,B1)",
    "=ADD(A1,B1)"
]
correct_answer = "=SUM(A1,B1)"
explanation = "SUM関数は複数のセルを合計する正しい関数です。"

# 質問を表示
st.subheader("問題:")
st.write(question)

# 選択肢の表示
user_answer = st.radio("正しい関数を1つ選んでください:", options)

# 回答ボタン
if st.button("答えを表示"):
    st.markdown(f"**あなたの回答：** {user_answer}")
    st.markdown(f"**正解：** {correct_answer}")
    
    # 判定
    if user_answer == correct_answer:
        st.success("正解です！🎉")
    else:
        st.error("不正解です。")

    # 解説
    st.info(f"💡 解説：{explanation}")
