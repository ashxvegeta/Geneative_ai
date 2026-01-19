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

prommpt = templete.format()
model_response = model.invoke(prommpt)

# print("Model Response:", model_response) //for seeing raw model response
parsed_output = parser.parse(model_response.content)
# print("Parsed Output:", parsed_output['name'])
print("Parsed Output:", parsed_output)

