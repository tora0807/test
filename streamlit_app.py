import streamlit as st
import random

# 占いの結果のリスト
fortune_results = [
    "今日は素晴らしい一日になりそうです！積極的に行動しましょう。",
    "少しの努力で大きな成果が期待できる日です。自信を持って進んでください。",
    "少しストレスを感じるかもしれませんが、冷静に対応すれば問題なし。",
    "今日はリラックスして過ごすことが吉です。無理せず休息を取ると良いでしょう。",
    "人とのコミュニケーションがカギになります。新しい出会いに期待大！"
]

# アプリのタイトル
st.title("ランダム占いアプリ")

# 占いボタン
if st.button('占ってみる'):
    result = random.choice(fortune_results)
    st.write(result)
