import streamlit as st

# 100問の医学クイズデータ（10セット×10問）
quiz_data = [
    # 第1セット
    {"set":1, "question":"正常な体温はおおよそ何度ですか？", "options":["35.0℃","36.5℃","37.5℃","38.0℃"], "answer":"36.5℃"},
    {"set":1, "question":"赤血球の主な役割は？", "options":["免疫防御","酸素運搬","ホルモン調整","栄養吸収"], "answer":"酸素運搬"},
    {"set":1, "question":"血圧の単位は？", "options":["mmHg","kPa","Pa","atm"], "answer":"mmHg"},
    {"set":1, "question":"心臓の左心室から出る血管は？", "options":["大動脈","肺動脈","静脈","冠状動脈"], "answer":"大動脈"},
    {"set":1, "question":"インスリンを分泌する臓器は？", "options":["膵臓","肝臓","腎臓","心臓"], "answer":"膵臓"},
    {"set":1, "question":"ビタミンCの別名は？", "options":["アスコルビン酸","リボフラビン","ニコチン酸","パントテン酸"], "answer":"アスコルビン酸"},
    {"set":1, "question":"肝臓で合成される血液成分は？", "options":["アルブミン","ヘモグロビン","フィブリン","インスリン"], "answer":"アルブミン"},
    {"set":1, "question":"肺で行われる主な機能は？", "options":["ガス交換","栄養吸収","免疫反応","血液凝固"], "answer":"ガス交換"},
    {"set":1, "question":"脳の中心部にある自律神経の調節中枢は？", "options":["視床下部","大脳皮質","小脳","海馬"], "answer":"視床下部"},
    {"set":1, "question":"赤血球の寿命は？", "options":["約120日","約30日","約7日","約365日"], "answer":"約120日"},

    # 第2セット
    {"set":2, "question":"血液型O型の抗体は？", "options":["抗A抗体・抗B抗体","抗A抗体のみ","抗B抗体のみ","抗A抗体も抗B抗体もない"], "answer":"抗A抗体・抗B抗体"},
    {"set":2, "question":"骨格筋の主な特徴は？", "options":["随意筋","不随意筋","平滑筋","心筋"], "answer":"随意筋"},
    {"set":2, "question":"膵液に含まれない酵素は？", "options":["ラクターゼ","リパーゼ","アミラーゼ","トリプシン"], "answer":"ラクターゼ"},
    {"set":2, "question":"糖尿病の主な原因は？", "options":["インスリン分泌不足","成長ホルモン過剰","甲状腺ホルモン低下","副腎皮質ホルモン過剰"], "answer":"インスリン分泌不足"},
    {"set":2, "question":"心電図でP波は何を示す？", "options":["心房の脱分極","心室の脱分極","心房の再分極","心室の再分極"], "answer":"心房の脱分極"},
    {"set":2, "question":"骨の主成分は？", "options":["カルシウム塩","コラーゲン","脂肪","糖質"], "answer":"カルシウム塩"},
    {"set":2, "question":"ヘモグロビンは主に何を運搬？", "options":["酸素","二酸化炭素","栄養素","ホルモン"], "answer":"酸素"},
    {"set":2, "question":"視覚を司る脳の部位は？", "options":["後頭葉","側頭葉","前頭葉","頭頂葉"], "answer":"後頭葉"},
    {"set":2, "question":"ビタミンDの主な役割は？", "options":["カルシウム吸収促進","免疫抑制","血糖調節","血液凝固"], "answer":"カルシウム吸収促進"},
    {"set":2, "question":"腎臓の機能は？", "options":["尿生成","消化","呼吸","免疫"], "answer":"尿生成"},

    # 第3セット
    {"set":3, "question":"肝臓の解毒作用で重要なのは？", "options":["シトクロムP450","カタラーゼ","リパーゼ","アミラーゼ"], "answer":"シトクロムP450"},
    {"set":3, "question":"免疫グロブリンの略称は？", "options":["Ig","Hb","DNA","RNA"], "answer":"Ig"},
    {"set":3, "question":"高血圧の基準は？", "options":["140/90 mmHg以上","120/80 mmHg以下","100/60 mmHg以下","160/100 mmHg以上"], "answer":"140/90 mmHg以上"},
    {"set":3, "question":"心臓の右心房に流入する血管は？", "options":["上大静脈","下大静脈","肺静脈","大動脈"], "answer":"上大静脈"},
    {"set":3, "question":"甲状腺ホルモンの主な役割は？", "options":["代謝促進","免疫抑制","血糖上昇","血圧低下"], "answer":"代謝促進"},
    {"set":3, "question":"白血球の一種で病原体を食べる細胞は？", "options":["好中球","赤血球","血小板","リンパ球"], "answer":"好中球"},
    {"set":3, "question":"肺胞で起こるのは？", "options":["ガス交換","血液凝固","栄養吸収","電気伝導"], "answer":"ガス交換"},
    {"set":3, "question":"骨髄で作られる細胞は？", "options":["血球","筋細胞","神経細胞","肝細胞"], "answer":"血球"},
    {"set":3, "question":"尿中の主要な廃棄物は？", "options":["尿素","グルコース","脂質","タンパク質"], "answer":"尿素"},
    {"set":3, "question":"脳卒中の主なタイプは？", "options":["虚血性・出血性","感染性","腫瘍性","変性性"], "answer":"虚血性・出血性"},

    # 第4セット
    {"set":4, "question":"血糖値を下げるホルモンは？", "options":["インスリン","グルカゴン","アドレナリン","コルチゾール"], "answer":"インスリン"},
    {"set":4, "question":"心臓の拍動を司るのは？", "options":["洞房結節","房室結節","心筋","弁膜"], "answer":"洞房結節"},
    {"set":4, "question":"赤血球の形状は？", "options":["円盤状（両面陥凹）","球状","棒状","三角形"], "answer":"円盤状（両面陥凹）"},
    {"set":4, "question":"抗生物質の作用は？", "options":["細菌の増殖抑制","ウイルスの増殖抑制","細胞の増殖促進","免疫抑制"], "answer":"細菌の増殖抑制"},
    {"set":4, "question":"肺の表面を覆う液体は？", "options":["肺サーファクタント","水分","血液","リンパ液"], "answer":"肺サーファクタント"},
    {"set":4, "question":"肝硬変の主な原因は？", "options":["アルコール","糖尿病","高血圧","肥満"], "answer":"アルコール"},
    {"set":4, "question":"血液のpHは？", "options":["約7.4","約6.8","約8.0","約5.5"], "answer":"約7.4"},
    {"set":4, "question":"血液凝固に関与するタンパク質は？", "options":["フィブリン","ヘモグロビン","アルブミン","インスリン"], "answer":"フィブリン"},
    {"set":4, "question":"脳の神経細胞の名称は？", "options":["ニューロン","グリア細胞","筋細胞","肝細胞"], "answer":"ニューロン"},
    {"set":4, "question":"甲状腺機能低下症の症状は？", "options":["疲労感","興奮","動悸","発汗"], "answer":"疲労感"},

    # 第5セット
    {"set":5, "question":"血液型AB型の抗体は？", "options":["なし","抗A抗体","抗B抗体","抗A抗体・抗B抗体"], "answer":"なし"},
    {"set":5, "question":"心臓の弁は何を防ぐ？", "options":["逆流","血液凝固","感染","電気信号"], "answer":"逆流"},
    {"set":5, "question":"骨の成長を促進するホルモンは？", "options":["成長ホルモン","甲状腺ホルモン","副腎皮質ホルモン","性ホルモン"], "answer":"成長ホルモン"},
    {"set":5, "question":"尿の主要な成分は？", "options":["水分","タンパク質","脂質","糖"], "answer":"水分"},
    {"set":5, "question":"細胞のエネルギー通貨は？", "options":["ATP","DNA","RNA","脂質"], "answer":"ATP"},
    {"set":5, "question":"肝臓で作られる胆汁の役割は？", "options":["脂肪の乳化","糖の分解","タンパク質合成","血液凝固"], "answer":"脂肪の乳化"},
    {"set":5, "question":"血液中の白血球は？", "options":["免疫細胞","酸素運搬","栄養吸収","ホルモン分泌"], "answer":"免疫細胞"},
    {"set":5, "question":"骨格筋の特徴は？", "options":["随意筋","不随意筋","平滑筋","心筋"], "answer":"随意筋"},
    {"set":5, "question":"心電図のQRS波は？", "options":["心室の脱分極","心房の脱分極","心室の再分極","心房の再分極"], "answer":"心室の脱分極"},
    {"set":5, "question":"脳の記憶に関与する部位は？", "options":["海馬","小脳","視床下部","大脳基底核"], "answer":"海馬"},

    # 第6セット
    {"set":6, "question":"血液凝固に必要なビタミンは？", "options":["ビタミンK","ビタミンC","ビタミンD","ビタミンB12"], "answer":"ビタミンK"},
    {"set":6, "question":"肺胞の主な役割は？", "options":["酸素と二酸化炭素の交換","血液凝固","栄養吸収","免疫応答"], "answer":"酸素と二酸化炭素の交換"},
    {"set":6, "question":"糖尿病で増加する血液中の物質は？", "options":["グルコース","インスリン","ヘモグロビン","アドレナリン"], "answer":"グルコース"},
    {"set":6, "question":"免疫細胞の一つでウイルス感染細胞を攻撃するのは？", "options":["キラーT細胞","B細胞","マクロファージ","好中球"], "answer":"キラーT細胞"},
    {"set":6, "question":"脳の思考や判断を司る部位は？", "options":["前頭葉","側頭葉","後頭葉","小脳"], "answer":"前頭葉"},
    {"set":6, "question":"肝臓で貯蔵されるのは？", "options":["グリコーゲン","脂肪酸","アミノ酸","カルシウム"], "answer":"グリコーゲン"},
    {"set":6, "question":"腎臓の基本単位は？", "options":["ネフロン","アネロン","グロムリン","サルコメア"], "answer":"ネフロン"},
    {"set":6, "question":"筋肉収縮に必要なイオンは？", "options":["カルシウムイオン","ナトリウムイオン","カリウムイオン","塩素イオン"], "answer":"カルシウムイオン"},
    {"set":6, "question":"血液の液体成分は？", "options":["血漿","血球","リンパ","細胞液"], "answer":"血漿"},
    {"set":6, "question":"脳のバランスを司る部位は？", "options":["小脳","海馬","視床下部","脳幹"], "answer":"小脳"},

    # 第7セット
    {"set":7, "question":"血液中の赤血球の数は？", "options":["約500万個/μL","約100万個/μL","約50万個/μL","約10万個/μL"], "answer":"約500万個/μL"},
    {"set":7, "question":"脳の感覚情報を処理する部位は？", "options":["頭頂葉","前頭葉","側頭葉","後頭葉"], "answer":"頭頂葉"},
    {"set":7, "question":"ホルモンの伝達方法は？", "options":["血液を介した伝達","神経伝達","直接接触","気体の拡散"], "answer":"血液を介した伝達"},
    {"set":7, "question":"副腎から分泌されるホルモンは？", "options":["アドレナリン","インスリン","甲状腺ホルモン","成長ホルモン"], "answer":"アドレナリン"},
    {"set":7, "question":"神経細胞の接合部は？", "options":["シナプス","ニューロン","軸索","樹状突起"], "answer":"シナプス"},
    {"set":7, "question":"血液型A型の抗原は？", "options":["A抗原","B抗原","AB抗原","抗原なし"], "answer":"A抗原"},
    {"set":7, "question":"骨粗鬆症の原因は？", "options":["カルシウム不足","鉄不足","ビタミンC過剰","蛋白質過剰"], "answer":"カルシウム不足"},
    {"set":7, "question":"脳の言語機能を司る領域は？", "options":["ブローカ野","ウェルニッケ野","海馬","視床下部"], "answer":"ブローカ野"},
    {"set":7, "question":"尿酸の増加で起こる疾患は？", "options":["痛風","糖尿病","高血圧","肝炎"], "answer":"痛風"},
    {"set":7, "question":"呼吸筋に含まれるのは？", "options":["横隔膜","心筋","平滑筋","骨格筋（随意筋）"], "answer":"横隔膜"},

    # 第8セット
    {"set":8, "question":"神経伝達物質の代表例は？", "options":["アセチルコリン","インスリン","グルカゴン","アドレナリン"], "answer":"アセチルコリン"},
    {"set":8, "question":"血液型B型の抗体は？", "options":["抗A抗体","抗B抗体","抗AB抗体","抗原なし"], "answer":"抗A抗体"},
    {"set":8, "question":"膵臓のランゲルハンス島が分泌するのは？", "options":["インスリン","グルカゴン","アドレナリン","コルチゾール"], "answer":"インスリン"},
    {"set":8, "question":"骨の中にある骨細胞は？", "options":["骨細胞","軟骨細胞","筋細胞","神経細胞"], "answer":"骨細胞"},
    {"set":8, "question":"肝臓で解毒される物質は？", "options":["アンモニア","ブドウ糖","脂肪酸","ビタミン"], "answer":"アンモニア"},
    {"set":8, "question":"尿路結石の主成分は？", "options":["カルシウム塩","尿酸","尿素","リン酸"], "answer":"カルシウム塩"},
    {"set":8, "question":"免疫に関与する臓器は？", "options":["胸腺","膵臓","肝臓","腎臓"], "answer":"胸腺"},
    {"set":8, "question":"血液型AB型の特徴は？", "options":["すべての抗原を持つ","抗原なし","抗体あり","Rh陰性"], "answer":"すべての抗原を持つ"},
    {"set":8, "question":"皮膚の最外層は？", "options":["表皮","真皮","皮下組織","筋膜"], "answer":"表皮"},
    {"set":8, "question":"脳幹に含まれないのは？", "options":["大脳皮質","延髄","橋","中脳"], "answer":"大脳皮質"},

    # 第9セット
    {"set":9, "question":"血液中の血小板の役割は？", "options":["血液凝固","酸素運搬","免疫防御","栄養吸収"], "answer":"血液凝固"},
    {"set":9, "question":"脳の記憶に重要な物質は？", "options":["ニューロン","グリア細胞","ミエリン","アセチルコリン"], "answer":"ニューロン"},
    {"set":9, "question":"腎臓の機能単位は？", "options":["ネフロン","ボーマン嚢","尿細管","集合管"], "answer":"ネフロン"},
    {"set":9, "question":"インスリンの作用は？", "options":["血糖値を下げる","血糖値を上げる","血圧を上げる","血圧を下げる"], "answer":"血糖値を下げる"},
    {"set":9, "question":"免疫の第一防衛線は？", "options":["皮膚","白血球","抗体","リンパ節"], "answer":"皮膚"},
    {"set":9, "question":"骨の再生を助けるビタミンは？", "options":["ビタミンD","ビタミンC","ビタミンA","ビタミンB12"], "answer":"ビタミンD"},
    {"set":9, "question":"脳の感情を司る部位は？", "options":["扁桃体","海馬","視床下部","小脳"], "answer":"扁桃体"},
    {"set":9, "question":"血液型O型の特徴は？", "options":["抗原なし","抗体なし","Rh陽性のみ","すべての抗原"], "answer":"抗原なし"},
    {"set":9, "question":"肺の換気に関与する筋肉は？", "options":["横隔膜","心筋","骨格筋","平滑筋"], "answer":"横隔膜"},
    {"set":9, "question":"心拍数を調節する中枢は？", "options":["延髄","視床下部","大脳皮質","小脳"], "answer":"延髄"},

    # 第10セット
    {"set":10, "question":"脳の血液供給は？", "options":["内頚動脈と椎骨動脈","大動脈と肺動脈","腎動脈と肝動脈","上大静脈と下大静脈"], "answer":"内頚動脈と椎骨動脈"},
    {"set":10, "question":"甲状腺ホルモンの分泌を調節するのは？", "options":["視床下部","脳幹","小脳","海馬"], "answer":"視床下部"},
    {"set":10, "question":"赤血球の色は？", "options":["赤色","無色","黄色","青色"], "answer":"赤色"},
    {"set":10, "question":"糖尿病で障害される血管は？", "options":["細小血管","大動脈","肺動脈","冠状動脈"], "answer":"細小血管"},
    {"set":10, "question":"肝臓で合成されないものは？", "options":["ヘモグロビン","アルブミン","胆汁酸","血液凝固因子"], "answer":"ヘモグロビン"},
    {"set":10, "question":"脳脊髄液が循環する場所は？", "options":["脳室系","血管","リンパ管","気管"], "answer":"脳室系"},
    {"set":10, "question":"骨格筋に含まれるタンパク質は？", "options":["アクチンとミオシン","ヘモグロビン","コラーゲン","フィブリン"], "answer":"アクチンとミオシン"},
    {"set":10, "question":"肺の気管支は何の枝？", "options":["気管","食道","食道支","気管支支"], "answer":"気管"},
    {"set":10, "question":"血液の浸透圧を調節するのは？", "options":["ナトリウムイオン","カリウムイオン","カルシウムイオン","マグネシウムイオン"], "answer":"ナトリウムイオン"},
    {"set":10, "question":"免疫の記憶を担当する細胞は？", "options":["メモリーT細胞","好中球","マクロファージ","赤血球"], "answer":"メモリーT細胞"},
]

def quiz_app():
    st.title("医学知識クイズアプリ")

    # セッションステート初期化
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

    # 選択されたセットの問題リスト
    current_set_questions = [q for q in quiz_data if q["set"] == st.session_state.set_selected]

    # クイズ終了後の表示
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
        selected = st.radio("選択肢から答えを選んでください。", options, index=0, key="options_radio")
        st.session_state.selected_option = selected
        if st.button("回答する"):
            st.session_state.answered = True
            if selected == q["answer"]:
                st.session_state.score += 1
            st.experimental_rerun()
    else:
        st.write(f"正解は： {q['answer']}")
        if st.session_state.current_question < 9:
            if st.button("次の問題へ"):
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
