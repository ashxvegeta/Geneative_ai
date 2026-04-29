from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup

url = 'https://mangobaba.in/product_details/3/mango'

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)