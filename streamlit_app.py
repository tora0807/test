import streamlit as st

st.title("🧠 医学知識クイズアプリ")
st.markdown("各セット10問。4択クイズにチャレンジ！")

quiz_data = [
    # 第1セット
    {"set":1, "question":"正常な体温はおおよそ何度ですか？", "options":["35.0℃","36.5℃","37.5℃","38.0℃"], "answer":"36.5℃"},
    {"set":1, "question":"赤血球の主な役割は？", "options":["免疫防御","酸素運搬","ホルモン調整","栄養吸収"], "answer":"酸素運搬"},
    {"set":1, "question":"肺炎の主な原因菌は？", "options":["黄色ブドウ球菌","肺炎球菌","大腸菌","サルモネラ菌"], "answer":"肺炎球菌"},
    {"set":1, "question":"血圧の正常値は？", "options":["90/60 mmHg","120/80 mmHg","140/90 mmHg","160/100 mmHg"], "answer":"120/80 mmHg"},
    {"set":1, "question":"糖尿病で不足するホルモンは？", "options":["インスリン","アドレナリン","グルカゴン","コルチゾール"], "answer":"インスリン"},
    {"set":1, "question":"骨粗鬆症で減少するものは？", "options":["骨密度","筋肉量","脂肪量","血液量"], "answer":"骨密度"},
    {"set":1, "question":"心臓の右心房に入る血液は？", "options":["酸素豊富な血液","酸素不足の血液","栄養豊富な血液","老廃物を含む血液"], "answer":"酸素不足の血液"},
    {"set":1, "question":"ビタミンCの主な役割は？", "options":["抗酸化作用","血液凝固","ホルモン調節","カルシウム吸収"], "answer":"抗酸化作用"},
    {"set":1, "question":"肺活量を測る機械は？", "options":["スパイロメーター","心電計","血圧計","聴診器"], "answer":"スパイロメーター"},
    {"set":1, "question":"肝臓の主な働きは？", "options":["解毒作用","酸素運搬","免疫機能","ホルモン分泌"], "answer":"解毒作用"},

    # 第2セット
    {"set":2, "question":"インフルエンザの潜伏期間は？", "options":["1〜3日","5〜7日","7〜14日","14〜21日"], "answer":"1〜3日"},
    {"set":2, "question":"血液型O型の抗原は？", "options":["抗A・抗B抗原","抗A抗原のみ","抗B抗原のみ","抗原なし"], "answer":"抗原なし"},
    {"set":2, "question":"心電図のP波は何を示す？", "options":["心房の興奮","心室の興奮","心房の収縮","心室の収縮"], "answer":"心房の興奮"},
    {"set":2, "question":"血液凝固に必要なミネラルは？", "options":["カルシウム","鉄","マグネシウム","カリウム"], "answer":"カルシウム"},
    {"set":2, "question":"インスリンを分泌する臓器は？", "options":["膵臓","肝臓","腎臓","心臓"], "answer":"膵臓"},
    {"set":2, "question":"肺のガス交換が行われる場所は？", "options":["肺胞","気管","気管支","胸膜"], "answer":"肺胞"},
    {"set":2, "question":"甲状腺ホルモンの主な働きは？", "options":["新陳代謝促進","免疫調節","血糖調整","カルシウム吸収"], "answer":"新陳代謝促進"},
    {"set":2, "question":"赤血球の寿命は？", "options":["約120日","約30日","約60日","約180日"], "answer":"約120日"},
    {"set":2, "question":"免疫に関与する白血球は？", "options":["リンパ球","赤血球","血小板","肝細胞"], "answer":"リンパ球"},
    {"set":2, "question":"脳を保護している膜は？", "options":["髄膜","胸膜","腹膜","心膜"], "answer":"髄膜"},

    # 第3セット
    {"set":3, "question":"心拍数の正常範囲は？", "options":["60〜100 bpm","40〜60 bpm","100〜140 bpm","140〜180 bpm"], "answer":"60〜100 bpm"},
    {"set":3, "question":"骨髄で作られない細胞は？", "options":["神経細胞","赤血球","白血球","血小板"], "answer":"神経細胞"},
    {"set":3, "question":"肝硬変の主な原因は？", "options":["ウイルス感染","喫煙","アルコール","肥満"], "answer":"ウイルス感染"},
    {"set":3, "question":"血糖値を下げるホルモンは？", "options":["インスリン","グルカゴン","アドレナリン","コルチゾール"], "answer":"インスリン"},
    {"set":3, "question":"骨折した時に最初にできる組織は？", "options":["血腫","軟骨","骨膜","筋肉"], "answer":"血腫"},
    {"set":3, "question":"肺炎球菌はどの臓器に感染？", "options":["肺","肝臓","腎臓","心臓"], "answer":"肺"},
    {"set":3, "question":"脳の記憶に関与する部分は？", "options":["海馬","小脳","視床","大脳皮質"], "answer":"海馬"},
    {"set":3, "question":"赤血球に含まれる酸素運搬タンパクは？", "options":["ヘモグロビン","ミオグロビン","コラーゲン","アルブミン"], "answer":"ヘモグロビン"},
    {"set":3, "question":"心不全の症状に含まれないのは？", "options":["発疹","浮腫","息切れ","咳"], "answer":"発疹"},
    {"set":3, "question":"血液型AB型の抗体は？", "options":["なし","抗A抗体","抗B抗体","抗A抗体と抗B抗体"], "answer":"なし"},

    # 第4セット
    {"set":4, "question":"血圧の正常な範囲はどれか？", "options":["120/80 mmHg","90/60 mmHg","140/90 mmHg","160/100 mmHg"], "answer":"120/80 mmHg"},
    {"set":4, "question":"白血球の役割は？", "options":["酸素運搬","免疫防御","血液凝固","栄養輸送"], "answer":"免疫防御"},
    {"set":4, "question":"肝硬変の主な原因は？", "options":["ウイルス感染","喫煙","過剰な運動","ストレス"], "answer":"ウイルス感染"},
    {"set":4, "question":"インフルエンザワクチンの接種時期は？", "options":["冬季前","夏季","春季","秋季前"], "answer":"秋季前"},
    {"set":4, "question":"ビタミンDの主な作用は？", "options":["骨のカルシウム吸収促進","血糖調節","酸素運搬","筋肉収縮"], "answer":"骨のカルシウム吸収促進"},
    {"set":4, "question":"心電図のP波は何を示すか？", "options":["心房の興奮","心室の興奮","心房の収縮","心室の収縮"], "answer":"心房の興奮"},
    {"set":4, "question":"免疫に関与する細胞は？", "options":["リンパ球","赤血球","血小板","筋細胞"], "answer":"リンパ球"},
    {"set":4, "question":"腎臓の機能は？", "options":["尿生成","血液凝固","免疫防御","酸素運搬"], "answer":"尿生成"},
    {"set":4, "question":"骨髄で産生される細胞は？", "options":["血球細胞","筋細胞","神経細胞","肝細胞"], "answer":"血球細胞"},
    {"set":4, "question":"脳の記憶に関わる部位は？", "options":["海馬","小脳","脳幹","脊髄"], "answer":"海馬"},

    # 第5セット
    {"set":5, "question":"腎臓の基本単位は？", "options":["ネフロン","ボーマン嚢","尿細管","集合管"], "answer":"ネフロン"},
    {"set":5, "question":"心臓の弁で右心房と右心室をつなぐのは？", "options":["三尖弁","僧帽弁","大動脈弁","肺動脈弁"], "answer":"三尖弁"},
    {"set":5, "question":"免疫グロブリンの種類でアレルギーに関与するのは？", "options":["IgE","IgG","IgA","IgM"], "answer":"IgE"},
    {"set":5, "question":"肺の表面を覆う膜は？", "options":["胸膜","腹膜","心膜","髄膜"], "answer":"胸膜"},
    {"set":5, "question":"貧血の主な原因は？", "options":["鉄欠乏","ビタミンD欠乏","カルシウム欠乏","ナトリウム欠乏"], "answer":"鉄欠乏"},
    {"set":5, "question":"血液型AB型はどの抗体を持つ？", "options":["なし","抗A抗体","抗B抗体","抗A抗体と抗B抗体"], "answer":"なし"},
    {"set":5, "question":"肝臓の働きに含まれないのは？", "options":["酸素運搬","解毒","代謝調節","胆汁生成"], "answer":"酸素運搬"},
    {"set":5, "question":"脳の主なエネルギー源は？", "options":["グルコース","脂肪酸","アミノ酸","乳酸"], "answer":"グルコース"},
    {"set":5, "question":"心拍数の正常値は？", "options":["60〜100回/分","40〜60回/分","100〜120回/分","120〜140回/分"], "answer":"60〜100回/分"},
    {"set":5, "question":"肺胞で行われることは？", "options":["ガス交換","血液凝固","免疫反応","栄養吸収"], "answer":"ガス交換"},

    # 第6セット
    {"set":6, "question":"糖尿病で不足するホルモンは？", "options":["インスリン","グルカゴン","アドレナリン","コルチゾール"], "answer":"インスリン"},
    {"set":6, "question":"脳神経は何対ある？", "options":["12対","10対","8対","14対"], "answer":"12対"},
    {"set":6, "question":"心臓の左心室から出る血管は？", "options":["大動脈","肺動脈","静脈","冠状動脈"], "answer":"大動脈"},
    {"set":6, "question":"肝臓で作られないものは？", "options":["インスリン","胆汁","アルブミン","血液凝固因子"], "answer":"インスリン"},
    {"set":6, "question":"赤血球に含まれるタンパク質は？", "options":["ヘモグロビン","アルブミン","フィブリン","コラーゲン"], "answer":"ヘモグロビン"},
    {"set":6, "question":"骨折修復で最初に形成される組織は？", "options":["血腫","軟骨","骨芽細胞","筋肉"], "answer":"血腫"},
    {"set":6, "question":"免疫系の中心的な細胞は？", "options":["リンパ球","赤血球","血小板","線維芽細胞"], "answer":"リンパ球"},
    {"set":6, "question":"肝硬変の主な原因は？", "options":["B型肝炎ウイルス","心不全","糖尿病","肥満"], "answer":"B型肝炎ウイルス"},
    {"set":6, "question":"脳の記憶を司る部位は？", "options":["海馬","小脳","大脳皮質","脳幹"], "answer":"海馬"},
    {"set":6, "question":"血液型A型の抗体は？", "options":["抗B抗体","抗A抗体","なし","両方あり"], "answer":"抗B抗体"},

    # 第7セット
    {"set":7, "question":"心電図でQRS波は何を示す？", "options":["心室の興奮","心房の興奮","心室の収縮","心房の収縮"], "answer":"心室の興奮"},
    {"set":7, "question":"血液凝固に必要な因子は？", "options":["カルシウム","鉄","マグネシウム","カリウム"], "answer":"カルシウム"},
    {"set":7, "question":"アレルギー反応に関与する抗体は？", "options":["IgE","IgG","IgA","IgM"], "answer":"IgE"},
    {"set":7, "question":"肺炎球菌はどの臓器に感染？", "options":["肺","肝臓","腎臓","心臓"], "answer":"肺"},
    {"set":7, "question":"骨粗鬆症で減少するものは？", "options":["骨密度","筋肉量","脂肪量","血液量"], "answer":"骨密度"},
    {"set":7, "question":"肝臓の主な働きは？", "options":["解毒作用","酸素運搬","免疫機能","ホルモン分泌"], "answer":"解毒作用"},
    {"set":7, "question":"心不全の症状に含まれないのは？", "options":["発疹","浮腫","息切れ","咳"], "answer":"発疹"},
    {"set":7, "question":"血液型Rh因子は？", "options":["赤血球表面のタンパク質","血漿の成分","血小板の一種","白血球の受容体"], "answer":"赤血球表面のタンパク質"},
    {"set":7, "question":"腎臓の機能に含まれないものは？", "options":["消化","排泄","ホルモン分泌","血圧調整"], "answer":"消化"},
    {"set":7, "question":"脳を保護する膜は？", "options":["髄膜","胸膜","腹膜","心膜"], "answer":"髄膜"},

    # 第8セット
    {"set":8, "question":"血糖値を上げるホルモンは？", "options":["グルカゴン","インスリン","アドレナリン","セロトニン"], "answer":"グルカゴン"},
    {"set":8, "question":"骨髄で作られない細胞は？", "options":["神経細胞","赤血球","白血球","血小板"], "answer":"神経細胞"},
    {"set":8, "question":"肺のガス交換場所は？", "options":["肺胞","気管","気管支","胸膜"], "answer":"肺胞"},
    {"set":8, "question":"腎臓の基本単位は？", "options":["ネフロン","ボーマン嚢","尿細管","集合管"], "answer":"ネフロン"},
    {"set":8, "question":"赤血球の寿命は？", "options":["約120日","約30日","約60日","約180日"], "answer":"約120日"},
    {"set":8, "question":"免疫に関与する白血球は？", "options":["リンパ球","赤血球","血小板","肝細胞"], "answer":"リンパ球"},
    {"set":8, "question":"抗生物質が効かないものは？", "options":["ウイルス感染","細菌感染","真菌感染","寄生虫感染"], "answer":"ウイルス感染"},
    {"set":8, "question":"血液型O型の抗原は？", "options":["抗A・抗B抗原","抗A抗原のみ","抗B抗原のみ","抗原なし"], "answer":"抗原なし"},
    {"set":8, "question":"心電図のQRS波は？", "options":["心室の興奮","心房の興奮","心室の収縮","心房の収縮"], "answer":"心室の興奮"},
    {"set":8, "question":"脂質異常症の診断に用いるのは？", "options":["血中コレステロール値","血糖値","血圧","体重"], "answer":"血中コレステロール値"},

    # 第9セット
    {"set":9, "question":"肝臓での解毒作用は？", "options":["薬物代謝","酸素運搬","免疫機能","血液凝固"], "answer":"薬物代謝"},
    {"set":9, "question":"貧血の原因でないのは？", "options":["脱水","鉄欠乏","ビタミンB12欠乏","慢性出血"], "answer":"脱水"},
    {"set":9, "question":"糖尿病治療薬でないのは？", "options":["抗生物質","インスリン","ビグアナイド","スルホニル尿素"], "answer":"抗生物質"},
    {"set":9, "question":"骨折修復で最後にできる組織は？", "options":["骨組織","血腫","軟骨","線維組織"], "answer":"骨組織"},
    {"set":9, "question":"心臓の左心房に入る血管は？", "options":["肺静脈","肺動脈","大動脈","上大静脈"], "answer":"肺静脈"},
    {"set":9, "question":"血液型B型の抗体は？", "options":["抗A抗体","抗B抗体","なし","両方あり"], "answer":"抗A抗体"},
    {"set":9, "question":"肺胞で交換されるガスは？", "options":["酸素と二酸化炭素","酸素と窒素","二酸化炭素と窒素","酸素と一酸化炭素"], "answer":"酸素と二酸化炭素"},
    {"set":9, "question":"肝臓の主要な細胞は？", "options":["肝細胞","腎細胞","筋細胞","神経細胞"], "answer":"肝細胞"},
    {"set":9, "question":"甲状腺ホルモンが不足すると？", "options":["代謝低下","代謝亢進","免疫力増強","血糖上昇"], "answer":"代謝低下"},
    {"set":9, "question":"血液中の主な塩類は？", "options":["ナトリウムイオン","カルシウムイオン","鉄イオン","マグネシウムイオン"], "answer":"ナトリウムイオン"},

    # 第10セット
    {"set":10, "question":"脳卒中の主な原因は？", "options":["高血圧","低血糖","貧血","糖尿病"], "answer":"高血圧"},
    {"set":10, "question":"肺の機能は？", "options":["呼吸によるガス交換","消化吸収","血液生成","免疫機能"], "answer":"呼吸によるガス交換"},
    {"set":10, "question":"糖尿病で異常が起こる臓器は？", "options":["膵臓","肝臓","腎臓","心臓"], "answer":"膵臓"},
    {"set":10, "question":"血液中の酸素運搬タンパク質は？", "options":["ヘモグロビン","アルブミン","フィブリン","コラーゲン"], "answer":"ヘモグロビン"},
    {"set":10, "question":"血液凝固に関与する細胞は？", "options":["血小板","赤血球","白血球","筋細胞"], "answer":"血小板"},
    {"set":10, "question":"骨の主成分は？", "options":["カルシウム塩","コラーゲン","脂肪","グルコース"], "answer":"カルシウム塩"},
    {"set":10, "question":"心拍数の正常範囲は？", "options":["60〜100回/分","40〜60回/分","100〜140回/分","140〜180回/分"], "answer":"60〜100回/分"},
    {"set":10, "question":"脳の部位で運動を司るのは？", "options":["大脳皮質運動野","小脳","脳幹","海馬"], "answer":"大脳皮質運動野"},
    {"set":10, "question":"インフルエンザの予防法は？", "options":["ワクチン接種","抗生物質服用","過度の運動","水分制限"], "answer":"ワクチン接種"},
    {"set":10, "question":"腎臓の機能は？", "options":["尿生成","血液凝固","呼吸調節","栄養吸収"], "answer":"尿生成"},
]

def quiz_app():
    if "set_selected" not in st.session_state:
        st.session_state.set_selected = None
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "user_answer" not in st.session_state:
        st.session_state.user_answer = None

    if st.session_state.set_selected is None:
        st.subheader("挑戦するセットを選んでください")
        set_choice = st.selectbox("セットを選択", options=[i for i in range(1,11)], index=0)
        if st.button("開始"):
            st.session_state.set_selected = set_choice
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.user_answer = None
            st.experimental_rerun()
    else:
        current_set = st.session_state.set_selected
        questions = [q for q in quiz_data if q["set"] == current_set]

        if st.session_state.question_index < len(questions):
            q = questions[st.session_state.question_index]
            st.write(f"### 問題 {st.session_state.question_index + 1} / {len(questions)}")
            st.write(q["question"])
            st.session_state.user_answer = st.radio("選択肢を選んでください", q["options"], index=0)

            if not st.session_state.answered:
                if st.button("回答する"):
                    st.session_state.answered = True
                    if st.session_state.user_answer == q["answer"]:
                        st.session_state.score += 1
                    st.experimental_rerun()
            else:
                correct = q["answer"]
                if st.session_state.user_answer == correct:
                    st.success("正解！")
                else:
                    st.error(f"不正解。正しい答えは「{correct}」です。")

                if st.button("次の問題へ"):
                    st.session_state.question_index += 1
                    st.session_state.answered = False
                    st.session_state.user_answer = None
                    st.experimental_rerun()
        else:
            st.write(f"🎉 セット{current_set}は終了です。")
            st.write(f"あなたの得点は {st.session_state.score} / {len(questions)} 問でした。")
            if st.button("別のセットを選ぶ"):
                st.session_state.set_selected = None
                st.session_state.question_index = 0
                st.session_state.score = 0
                st.session_state.answered = False
                st.session_state.user_answer = None
                st.experimental_rerun()

if __name__ == "__main__":
    quiz_app()
