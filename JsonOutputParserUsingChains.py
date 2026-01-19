from html import parser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm,temperature=0)

parser = JsonOutputParser()

templete= PromptTemplate(
    template="give me the name,age and city of a fictional person\n {fomat_instructions}" ,
    input_variables=[],
    partial_variables={"fomat_instructions": parser.get_format_instructions()}
)

chain = templete | model | parser
# in this case no input variables are needed so we pass an empty dict
result = chain.invoke({})
print("Parsed Output:", result)