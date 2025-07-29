import streamlit as st

st.set_page_config(page_title="医学クイズアプリ", page_icon="🩺")

st.title("🩺 医学クイズアプリ")

# クイズの設定
question = "次のうち、糖尿病の三大症状に含まれないものはどれ？"
options = ["多尿", "多飲", "頻脈", "多食"]
correct_answer = "頻脈"
explanation = "糖尿病の三大症状は「多尿・多飲・多食」です。「頻脈」は含まれません。"

# 問題の表示
st.subheader("問題:")
st.write(question)

# 選択肢の表示
user_answer = st.radio("選択肢を選んでください:", options)

# 答え合わせボタン
if st.button("答え合わせ"):
    # ユーザーの回答表示
    st.markdown(f"**あなたの回答：** {user_answer}")
    st.markdown(f"**模範解答：** {correct_answer}")

    # 判定
    if user_answer == correct_answer:
        st.success("正解です！🎉")
    else:
        st.error("不正解です。")

    # 解説表示
    st.info(f"💡 解説：{explanation}")
