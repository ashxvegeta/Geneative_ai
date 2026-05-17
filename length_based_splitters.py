from langchain_text_splitters import CharacterTextSplitter

text = "This is a long text that needs to be split into smaller chunks. The text splitter will divide the text based on a specified length, ensuring that each chunk is manageable and easy to process."

splitter = CharacterTextSplitter( separator="",chunk_size=20, chunk_overlap=0,)
result = splitter.split_text(text)
print(result)