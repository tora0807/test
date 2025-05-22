# streamlit_template

st.title("あいうえお“)

st.write("aiueo")

user_name=st.text_input("名前を入力してください")

st.header("あなたの名前は“＋st(user_name)+"です")

h=st.number_input("身長を入力してください(ｍ)",value=1.70)
w=st.number_input("体重を入力してください（kg)",value=70)

bmi=w/(h**2)

dbmi=round(bmi,2)

st.header("あなたのBMIは"+str(dbmi)+"です")

