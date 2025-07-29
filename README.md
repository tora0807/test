import streamlit as st
import pandas as pd

# === Excelファイルから読み込み ===
@st.cache_data
def load_questions():
    df = pd.read_excel("問題集.xlsx")
    return df

df = load_questions()

# ==== セッション状態の初期化 ====
if "q_num" not in st.session_state:
    st.session_state.q_num = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False

# ==== 現在の問題取得 ====
if st.session_state.q_num < len(df):
    current = df.iloc[st.session_state.q_num]
    
    st.title("📘 Excel 学習問題（Excelファイルから読み取り）")
    st.subheader(f"問題 {int(current['番号'])} / {len(df)}")
    st.write(current["問題文"])

    # ==== 選択肢 ====
    choices = ["①", "②", "③", "④"]
    for i, choice in enumerate(choices):
        st.write(f"{choice}: {current[choice]}")

    # ==== 答え表示 ====
    if st.button("✅ 正解を見る"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        correct_choice = current["正解"]
        correct_text = current[correct_choice]
        st.success(f"正解は {correct_choice}：{correct_text}")

    # ==== 次の問題へ ====
    if st.button("➡️ 次の問題へ"):
        if st.session_state.q_num < len(df) - 1:
            st.session_state.q_num += 1
            st.session_state.show_answer = False
        else:
            st.success("すべての問題が終了しました！お疲れ様でした。")
else:
    st.success("すべての問題が終了しました！")
