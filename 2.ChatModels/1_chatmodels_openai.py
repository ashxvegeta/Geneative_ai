from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
model = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    max_completion_tokens=10
) # Initialize the OpenAI Chat LLM with the specified model
result = model.invoke("what is the capital of india?")  # Call the Chat LLM to get the capital of India
print(result.content)  # Print the result