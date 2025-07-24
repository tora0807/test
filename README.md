import streamlit as st

st.title("医学クイズアプリ")

# --- 症例 ---
st.subheader("【問題】")
st.write("""
35歳の男性が発熱と咳を主訴に来院した。胸部X線で右下肺野に浸潤影を認めた。
最も考えられる疾患はどれか？
""")

# --- 選択肢 ---
options = [
    "気管支喘息",
    "肺炎",
    "肺癌",
    "肺血栓塞栓症"
]
user_choice = st.radio("選択肢を選んでください：", options)

# --- 状態管理（ボタンを押したときだけ回答を表示）---
if "show_med_answer" not in st.session_state:
    st.session_stat_
