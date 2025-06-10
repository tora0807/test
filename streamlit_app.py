import streamlit as st
import random

# じゃんけんの手
choices = ["グー", "チョキ", "パー"]

# ヘッダー
st.title("✋✌️✊ じゃんけんゲーム")

# ユーザーが選べるオプション
user_choice = st.selectbox("あなたの手を選んでください:", choices)

# コンピューターの選択をランダムに決定
compute
