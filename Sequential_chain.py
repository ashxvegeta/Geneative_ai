from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detail report on {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Generate a summary of the following report: {report}",
    input_variables=["report"]
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
final_result_chain = chain.invoke({"topic": "Sarvam Ai in india"})
print("Parsed Output:", final_result_chain)