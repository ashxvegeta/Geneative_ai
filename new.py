from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()  # Load environment variables from .env file
llm = ChatOpenAI(model="gpt-4o-mini")  # Initialize the OpenAI LLM with the specified model
result = llm.invoke("Tell me a joke about programming.")  # Call the LLM to generate a joke about programming
print(result)  # Print the generated joke