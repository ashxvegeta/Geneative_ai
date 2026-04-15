from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda ,RunnableBranch   

load_dotenv()

prompt1 = PromptTemplate(
    template="write a detailed report on {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize  the following text \n {text}.",   
    input_variables=["text"]
)

model = ChatOpenAI()

parser = StrOutputParser()


report_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300,RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
    
)
final_chain = RunnableSequence(report_chain, branch_chain) 
print(final_chain.invoke({"topic": "the impact of artificial intelligence on society"}))