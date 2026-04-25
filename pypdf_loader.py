from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('multipage_test_document.pdf')
docs = loader.load()
print(docs)
print(len(docs))
print(docs[0].page_content)  #to get only first page data
print(docs[0].metadata) # to print the metadata