from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('multipage_test_document.pdf')
documents = loader.load()


splitter = CharacterTextSplitter( separator="",chunk_size=20, chunk_overlap=0,)
result = splitter.split_documents(documents)
# print(result)
print(result[0].page_content)  #to get only first page data
print(result[0].metadata) # to print the metadata