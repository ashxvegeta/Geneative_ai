# It basically lets LangChain talk to OpenAI models using your API key.
from langchain_openai import OpenAI

# It’s used to load environment variables (like your OPENAI_API_KEY) from a file named .env into your Python program automatically.
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
) # Initialize the OpenAI LLM with the specified model

result = llm.invoke("Tell me a joke about programming.")  # Call the LLM to generate a joke about programming

print(result)  # Print the generated joke