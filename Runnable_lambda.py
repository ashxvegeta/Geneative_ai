# from langchain_core.runnables import RunnableLambda


# def word_counter(text: str) -> int:
#     """Counts the number of words in a given text."""
#     return len(text.split())

# # Create a RunnableLambda that wraps the word_counter function
# word_count_runnable = RunnableLambda(word_counter)
# # Example usage
# text = "Hello world! This is a test."
# count = word_count_runnable.invoke(text)
# print(f"The number of words in the text is: {count}")

# ---------------------above code is normal lambda fucntion usage---------------------

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda    

load_dotenv()

def word_counter(text: str) -> int:
    """Counts the number of words in a given text."""
    return len(text.split())

# Prompt
prompt = PromptTemplate(
    template="Tell me a joke about {topic}.",
    input_variables=["topic"]
)
# LLM
llm = ChatOpenAI() 
# Parser
parser = StrOutputParser()


# Chain
joke_generator_chain = RunnableSequence(prompt, llm, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_counter)  
})

final_chain = RunnableSequence(joke_generator_chain, parallel_chain)
# Run
print(final_chain.invoke({"topic": "programming"}))
