import streamlit as st
import pandas as pd
import math

# === 問題データ読み込み ===
@st.cache_data
def load_questions():
    return pd.read_excel("問題集.xlsx")

df = load_questions()
total_questions = len(df)
questions_per_set = 10
total_sets = math.ceil(total_questions / questions_per_set)

# === セッション状態の初期化 ===
if "set_index" not in st.session_state:
    st.session_state.set_index = 0  # 今のセット（0=最初の10問）
if "q_index" not in st.session_state:
    st.session_state.q_index = 0  # セット内の問題番号（0〜9）
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "answered" not in st.session_state:
    st.session_state.answered = False

# === 現在の問題取得 ===
start = st.session_state.set_index * questions_per_set
end = min(start + questions_per_set, total_questions)

subset = df.iloc[start:end].reset_index(drop=True)

if st.session_state.q_index < len(subset):
    current = subset.iloc[st.session_state.q_index]

    st.title("📘 Excel 医学知識クイズ")
    st.markdown(f"**第 {st.session_state.set_index + 1} セット（{start + 1}〜{end} 問）**")
    st.subheader(f"問題 {int(current['番号'])}")
    st.write(current["問題文"])

    # 選択肢の表示
    choices = ["①", "②", "③", "④"]
    options = [f"{c}: {current[c]}" for c in choices]
    user_choice = st.radio("選択肢を選んでください：", options, index=None, key=f"radio_{st.session_state.q_index}")

    # 解答ボタン
    if st.button("解答する"):
        if user_choice:
            st.session_state.user_answer = user_choice.split(":")[0]
            st.session_state.answered = True
        else:
            st.warning("選択肢を選んでください。")

    # 解答後の表示
    if st.session_state.answered:
        correct = current["正解"]
        if st.session_state.user_answer == correct:
            st.success(f"✅ 正解です！（{correct}: {current[correct]}）")
        else:
            st.error(f"❌ 不正解です。正解は {correct}: {current[correct]} です。")

        # 解説表示（任意）
        if "解説" in current and pd.notna(current["解説"]):
            st.info(f"📖 解説：{current['解説']}")

        # 次の問題へ
        if st.button("➡️ 次の問題へ"):
            st.session_state.q_index += 1
            st.session_state.user_answer = None
            st.session_state.answered = False
else:
    # すべての問題を解き終えた場合
    st.success(f"✅ 第 {st.session_state.set_index + 1} セット完了！")

    # 次のセットへ
    if st.session_state.set_index < total_sets - 1:
        if st.button("📚 次の10問へ"):
            st.session_state.set_index += 1
            st.session_state.q_index = 0
            st.session_state.user_answer = None
            st.session_state.answered = False
    else:
        st.balloons()
        st.success("🎉 全問題を解き終えました！お疲れさまでした。")
