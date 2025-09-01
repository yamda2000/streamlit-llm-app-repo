#from dotenv import load_dotenv
import streamlit as st
import os
from openai import OpenAI

#load_dotenv()
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("夏目漱石AIが回答してくれるアプリ")
st.write("質問を入力し、「実行」ボタンを押すことで、夏目漱石AIが回答してくれます。")

st.divider()

input_message = st.text_input(label="質問を入力してください。")
client=OpenAI()

if st.button("実行"):

    st.divider()

    if input_message:
        FT_MODEL = "ft:gpt-4.1-nano-2025-04-14:personal::CA3cbeMu"  # ←あなたのID

        resp = client.chat.completions.create(
        model=FT_MODEL,
        messages=[
            {"role": "system", "content":  "あなたは夏目漱石の口調・性格で、質問に対して名言を織り交ぜて回答するアシスタントAIです。"},
            {"role": "user", "content": input_message}
        ],
        )

        st.write("### 夏目漱石AI回答")
        st.write(resp.choices[0].message.content)

    else:
        st.error("質問が入力されていません。入力してください。")