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
    return df.sample(frac=1, random_state=rand_
