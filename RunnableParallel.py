from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

# LLM
llm = ChatOpenAI() 

# Parser
parser = StrOutputParser()

# Prompt1
prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}.",
    input_variables=["topic"]
)
#second prompt
prompt2 = PromptTemplate(
    template="Generate a LinkedIn post about {topic}.",
    input_variables=["topic"]
)
# Chain (modern way)
chain = RunnableParallel(
   {
    "tweet": RunnableSequence(prompt1, llm, parser),
    "linkedin": RunnableSequence(prompt2, llm, parser)
   }
)

# Run
result = chain.invoke({"topic": "programming"})

print(result)
