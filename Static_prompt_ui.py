from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
st.header("Research Tool")
#  take user_input
user_input = st.text_input("Enter your Prompt:")  
if st.button('Summerize'):
    model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    result  = model.invoke(user_input)
    st.write(result.content)
