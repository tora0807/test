import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Excel問題シャッフラー", page_icon="📊")

st.title("📊 Excel問題シャッフラー")

# ----------------------------
# Excelファイルの読み込み関数
# ----------------------------
@st.cache_data
def load_questions(file_path):
    df = pd.read_excel(file_path)
    return df.sample(frac=1, random_state=random.randint(0, 9999)).reset_index(drop=True)  # 毎回ランダム順

# ----------------------------
# ファイル読み込み
# ----------------------------
try:
    questions_df = load_questions("問題集.xlsx")
except Exception as e:
    st.error(f"Excelファイルの読み込みに失敗しました: {e}")
    st.stop()

# ----------------------------
# セッションの初期化
# ----------------------------
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# ----------------------------
# 問題の表示
# ----------------------------
index = st.session_state.current_index

if index < len(questions_df):
    question = questions_df.iloc[index]

    st.markdown(f"### 問題 {int(question['番号'])}")
    st.write(f"**{question['問題文']}**")

    choices = {
        "①": question["①"],
        "②": question["②"],
        "③": question["③"],
        "④": question["④"],
    }

    # 選択肢をシャッフルして表示
    shuffled_items = list(choices.items())
    random.shuffle(shuffled_items)

    selected = st.radio("選択肢を選んでください：", options=[f"{k}: {v}" for k, v in shuffled_items])

    # デバッグ用：選択された値を表示
    st.write(f"選択された選択肢: {selected}")

    if st.button("解答する"):
        selected_label = selected.split(":")[0]
        correct_label = question["正解"]

        # デバッグ用：正解を表示
        st.write(f"正解ラベル: {correct_label}")

        if selected_label == correct_label:
            st.success("✅ 正解！")
            st.session_state.score += 1
        else:
            correct_text = choices[correct_label]
            st.error(f"❌ 不正解！ 正解は「{correct_label}: {correct_text}」です。")

        st.session_state.current_index += 1
        st.rerun()  # 状態をリセットして再実行
else:
    st.markdown("### ✅ 全ての問題が終了しました。")
    st.markdown(f"**スコア: {st.session_state.score} / {len(questions_df)}**")

    if st.button("もう一度挑戦する"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.rerun()  # 状態をリセットして再実行
