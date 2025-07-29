import streamlit as st

st.set_page_config(page_title="医学クイズアプリ", page_icon="🩺")
st.title("🩺 医学クイズアプリ")

# 問題内容
question = "次のうち、糖尿病の三大症状に含まれないものはどれ？"
options = ["多尿", "多飲", "頻脈", "多食"]
correct_answer = "頻脈"
explanation = "糖尿病の三大症状は「多尿」「多飲」「多食」です。「頻脈」は含まれません。"

# 表示：問題
st.subheader("問題：")
st.write(question)

# 表示：選択肢
user_answer = st.radio("選択肢から答えを選んでください：", options)

# ボタンを押すと答えを表示
if st.button("解答を表示"):
