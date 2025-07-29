import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def forgetting_curve(days):
    return np.exp(-0.2 * days)

if 'answers' not in st.session_state:
    st.session_state.answers = []

# --- 問題提示・解答部分 --- #

# （たとえば、問題が n 問あるとして）
question_id = 1
if st.button(f"問題 {question_id} を解答"):
    st.session_state.answers.append({'id': question_id, 'date': pd.Timestamp.now().strftime("%Y-%m-%d")})

all_answered = len(st.session_state.answers) >= total_questions

if all_answered:
    fig, ax = plt.subplots()
    for ans in st.session_state.answers:
        days = np.arange(0, (pd.Timestamp.now().normalize() - pd.to_datetime(ans['date'])).days + 1)
        ax.plot(days, forgetting_curve(days), label=f"Q{ans['id']}")
    ax.set_xlabel("日数")
    ax.set_ylabel("記憶度")
    ax.legend()
    st.pyplot(fig)
