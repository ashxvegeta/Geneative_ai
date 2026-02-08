from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 intresting facts in single line about this {topic}?",
    input_variables=["topic"]
)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()
chain = prompt | model | parser
final_result_chain = chain.invoke({"topic": "space"})
print("Parsed Output:", final_result_chain)
