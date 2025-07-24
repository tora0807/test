import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🧠 忘却曲線グラフ（医学クイズ復習用）")

# 時間（時間単位）
time_hours = np.array([0, 0.33, 1, 24, 168, 720])  # 分, 1時間, 1日, 1週間, 1ヶ月
labels = ["直後", "20分後", "1時間後", "1日後", "1週間後", "1か月後"]

# 忘却曲線：指数関数（目安）
def forgetting_curve(t):
    return 100 * np.exp(-0.15 * t)  # 仮の減衰係数

retention = forgetting_curve(time_hours)

# グラフ描画
fig, ax = plt.subplots()
ax.plot(time_hours, retention, marker="o")
ax.set_title("エビングハウスの忘却曲線")
ax.set_xlabel("経過時間（時間）")
ax.set_ylabel("記憶保持率（%）")
ax.set_xticks(time_hours)
ax.set_xticklabels(labels)
ax.set_ylim(0, 100)
ax.grid(T
