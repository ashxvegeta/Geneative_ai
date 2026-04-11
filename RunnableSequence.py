from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

# Prompt
prompt = PromptTemplate(
    template="Tell me a joke about {topic}.",
    input_variables=["topic"]
)

# LLM
llm = ChatOpenAI() 

# Parser
parser = StrOutputParser()

# Chain (modern way)
chain = RunnableSequence(prompt, llm, parser)

# Run
result = chain.invoke({"topic": "programming"})

print(result)
