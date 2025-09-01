#from dotenv import load_dotenv
import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

#load_dotenv()
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("生成AIが回答してくれるWEBアプリ")
st.write("入力フォームに健康or資産形成に関する質問を入力し、「実行」ボタンを押すことで、専門家AIが回答してくれます。")


selected_item = st.radio(
    "専門家AIを選択してください。",
    ["健康の専門家AI", "資産形成の専門家AI"]
)


llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


st.divider()

if selected_item == "健康の専門家AI":
    system_message = "あなたは健康の専門家です。ユーザーからの健康に関する質問に対して、わかりやすく丁寧に回答してください。"
    input_message = st.text_input(label="健康に関する質問を入力してください。")
    ai_name="健康の専門家AI"
else:
    system_message = "あなたは資産形成の専門家です。ユーザーからの資産形成に関する質問に対して、わかりやすく丁寧に回答してください。"
    input_message = st.text_input(label="資産形成に関する質問を入力してください。")
    ai_name="資産形成の専門家AI"

if st.button("実行"):
    st.divider()

    if input_message:
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=input_message)
        ]
        result=llm(messages)
        st.write("### 専門家AI回答")
        st.write(result.content)

    else:
        st.error("質問が入力されていません。質問を入力してください。")