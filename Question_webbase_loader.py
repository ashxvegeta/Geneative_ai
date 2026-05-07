from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI() 
# Prompt
prompt = PromptTemplate(
    template="Answer the following question: /n {question} from the following webpage: /n {text}",
    input_variables=["question", "text"]
)
parser = StrOutputParser()
 
url = 'https://mangobaba.in/product_details/3/mango'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser
print(chain.invoke({"question": "What is the price of mango?", "text": docs[0].page_content}))