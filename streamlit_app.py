if all_answered:
    st.write("✅ 全問回答完了！忘却曲線を表示します")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    for ans in st.session_state.answers:
        days, mem = compute_memory_timeseries(ans['date'])
        ax.plot(days, mem, label=f"問題 {ans['id']}")
    ax.set_xlabel("日数")
    ax.set_ylabel("記憶度")
    ax.legend()
    st.pyplot(fig)
