from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm,temperature=0)

# 1st prompt
templete1= PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic'])

templete2= PromptTemplate(
    template='write a 5 line summery on the following text./n {text}',
    input_variables=['text'])

prompt1 = templete1.invoke({"topic": "climate change"})
result = model.invoke(prompt1)
prompt2 = templete2.invoke({'text': result.content})
result2 = model.invoke(prompt2)
print(result2.content)