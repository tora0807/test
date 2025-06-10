import streamlit as st
import random

# 運勢のリスト
fortunes = [
    "大吉：最高の運勢！今日は何をやってもうまくいくでしょう。",
    "中吉：良いことがありそうな予感！",
    "小吉：まあまあ良い日になりそうです。",
    "吉：普通の日。落ち着いて過ごしましょう。",
    "凶：注意が必要な日。無理せず慎重に。",
]

st.title("🎴 今日の運勢占いアプリ")

# 名前入力
name = st.text_input("あなたの名前を入力してください")

if st.button("占う"):
    if name.strip() == "":
        st.warning("名前を入力してくださいね！")
    else:
        fortune = random.choice(fortunes)
        st.write(f"{name}さんの今日の運勢は…")
        st.success(fortune)
