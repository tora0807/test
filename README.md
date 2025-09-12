import streamlit as st
import pandas as pd

# === 問題データ読み込み ===
@st.cache_data
def load_questions():
    return pd.read_excel("問題集.xlsx")

df = load_questions()

# === セッション状態 ===
if "q_num" not in st.session_state:
    st.session_state.q_num = 0
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "answered" not in st.session_state:
    st.session_state.answered = False

# === 現在の問題 ===
if st.session_state.q_num < len(df):
    current = df.iloc[st.session_state.q_num]
    st.title("📘 Excel 学習問題（1問ずつ選択・解説付き）")
    st.subheader(f"問題 {int(current['番号'])} / {len(df)}")
    st.write(current["問題文"])

    # 選択肢をラジオボタンで表示
    choices = ["①", "②", "③", "④"]
    options = [f"{c}: {current[c]}" for c in choices]
    user_choice = st.radio("選択肢を選んでください：", options, index=None)

    # 回答ボタン
    if st.button("解答する"):
        if user_choice:
            st.session_state.user_answer = user_choice.split(":")[0]
            st.session_state.answered = True
        else:
            st.warning("選択肢を選んでから解答してください。")

    # 解答後の表示
    if st.session_state.answered:
        correct = current["正解"]
        if st.session_state.user_answer == correct:
            st.success(f"✅ 正解です！({correct}: {current[correct]})")
        else:
            st.error(f"❌ 不正解です。正解は {correct}: {current[correct]} です。")
        # 解説表示（あれば）
        if "解説" in current and pd.notna(current["解説"]):
            st.info(f"📖 解説：{current['解説']}")

        # 次の問題へボタン
        if st.button("➡️ 次の問題へ"):
            st.session_state.q_num += 1
            st.session_state.user_answer = None
            st.session_state.answered = False
else:

    st.success("🎉 すべての問題が完了しました！")
