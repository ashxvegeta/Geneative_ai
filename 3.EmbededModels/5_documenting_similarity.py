from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)
documents = [
	"Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
	"MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
	"Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
	"Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
	"Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]
query = "tell me about virat kohli?"
# Generate embeddings for documents and the query
documents_embeddings = embeddings.embed_documents(documents)
# Generate embeddings for the query
query_embedding = embeddings.embed_query(query)

# Compute cosine similarities between the query and each document
score = cosine_similarity([query_embedding], documents_embeddings)[0]
index, score = sorted(list(enumerate(score)), key=lambda x: x[1])[-1]
print(query)
print(documents[index])
print(f"Most similar document index: {index}, score: {score}")
