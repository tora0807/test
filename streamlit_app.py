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
total_sets = math.ceil(total_q
