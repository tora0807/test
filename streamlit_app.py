import streamlit as st

quiz_data = [
    # （省略）ここに全100問を入れてください。以下例のみ。
    {"set":1, "question":"正常な体温はおおよそ何度ですか？", "options":["35.0℃","36.5℃","37.5℃","38.0℃"], "answer":"36.5℃"},
    {"set":1, "question":"赤血球の主な役割は？", "options":["免疫防御","酸素運搬","ホルモン調整","栄養吸収"], "answer":"酸素運搬"},
    # 他セット省略
]

def quiz_app():
    st.title("医学知識クイズアプリ")

    if "set_selected" not in st.session_state:
        st.session_state.set_selected = None
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "selected_option" not in st.session_state:
        st.session_state.selected_option = None
    if "finished" not in st.session_state:
        st.session_state.finished = False

    def select_set(set_num):
        st.session_state.set_selected = set_num
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.selected_option = None
        st.session_state.finished = False

    if st.session_state.set_selected is None:
        st.write("難易度セットを選択してください（1〜10）")
        sets = list(range(1, 11))
        for s in sets:
            st.button(f"第{s}セットを選ぶ", on_click=select_set, args=(s,))
        return

    current_set_questions = [q for q in quiz_data if q["set"] == st.session_state.set_selected]

    if st.session_state.finished:
        st.write(f"第{st.session_state.set_selected}セットは終了です。")
        st.write(f"あなたの正解数：{st.session_state.score} / 10")
        if st.button("別のセットを選ぶ"):
            st.session_state.set_selected = None
            st.experimental_rerun()
        return

    q = current_set_questions[st.session_state.current_question]

    st.write(f"第{st.session_state.set_selected}セット - 問題 {st.session_state.current_question + 1} / 10")
    st.write(q["question"])

    if not st.session_state.answered:
        options = q["options"]
        selected = st.radio("選択肢から答えを選んでください。", options, index=0, key=f"options_radio_{st.session_state.current_question}")
        st.session_state.selected_option = selected

        if st.button("回答する", key=f"answer_btn_{st.session_state.current_question}"):
            if st.session_state.selected_option is None:
                st.warning("選択肢を選んでください。")
            else:
                st.session_state.answered = True
                if st.session_state.selected_option == q["answer"]:
                    st.session_state.score += 1
                st.experimental_rerun()
    else:
        st.write(f"正解は： {q['answer']}")
        if st.session_state.current_question < 9:
            if st.button("次の問題へ", key=f"next_btn_{st.session_state.current_question}"):
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.session_state.selected_option = None
                st.experimental_rerun()
        else:
            if st.button("結果を見る"):
                st.session_state.finished = True
                st.experimental_rerun()

if __name__ == "__main__":
    quiz_app()
