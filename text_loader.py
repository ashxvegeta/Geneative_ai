from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI() 
# Prompt
prompt = PromptTemplate(
    template="write a summary about the following/n {poem}.",
    input_variables=["poem"]
)
parser = StrOutputParser()
loader = TextLoader("test.txt", encoding="utf-8")
documents = loader.load()
# print(documents)
# print(type(documents))
# print(len(documents))
# print(type(documents[0]))
# print(documents[0].page_content)
# print(documents[0].metadata)

chain = prompt | model | parser
print(chain.invoke({"poem": documents[0].page_content}))