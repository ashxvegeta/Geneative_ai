from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

# LLM
llm = ChatOpenAI() 

# Parser
parser = StrOutputParser()

# Prompt
prompt1 = PromptTemplate(
    template="Tell me a joke about {topic}.",
    input_variables=["topic"]
)
#second prompt
prompt2 = PromptTemplate(
    template="explain the following joke - {text}.",
    input_variables=["text"]
)

# Chain (modern way)
joke_generator_chain = RunnableSequence(prompt1, llm, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, llm, parser)
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

# Run
result = final_chain.invoke({"topic": "programming"})
print(result)
