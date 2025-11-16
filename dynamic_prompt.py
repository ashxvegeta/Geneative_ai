from langchain.chat_models import ChatOpenAI
# for old version of langchain
# from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import streamlit as st
# for new version of langchain
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()
st.header("Research Tool")
#  take user_input


paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need",
"BERT: Pre-training of Deep Bidirectional Transformers", "GPT -3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical","Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# load the dynaic prompt
template = load_prompt("template.json")  

# placeholder for output
prompt = template.invoke({"paper_input": paper_input, "style_input": style_input, "length_input": length_input})

if st.button('Summarize'):
    model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    result  = model.invoke(prompt)
    st.write(result.content)

