import numpy as np
import pandas as pd

def show_forgetting_curve():
    st.success("50問すべて解き終わりました！お疲れさまです🎉")
    st.subheader("📉 忘却曲線")

    # 時間軸と記憶率（指数関数的に減少）
    t = np.linspace(0, 72, 100)
    retention = np.exp(-0.05 * t)

    df = pd.DataFrame({
        '時間（時間）': t,
        '記憶率': retention
    })

    st.line_chart(df.rename(columns={'時間（時間）': 'index'}).set_index('index'))

    st.markdown("""
    ### 解説：
    - 忘却曲線は、時間の経過とともに記憶がどのように減少するかを表したものです。
    - 復習のタイミングを工夫することで、記憶を効率よく定着させられます。
    - 例えば、**24時間以内の復習**が非常に効果的です。
                
    """)
