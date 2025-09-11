import streamlit as st
import numpy as np
import pandas as pd

def show_forgetting_curve():
    st.write("忘却曲線のグラフ")

    t = np.linspace(0, 24, 100)
    retention = np.exp(-0.1 * t)

    df = pd.DataFrame({
        '時間（時間）': t,
        '記憶率': retention
    })

    st.line_chart(df.rename(columns={'時間（時間）': 'index'}).set_index('index'))

# 呼び出し例（10問解いた後などに）
show_forgetting_curve()
