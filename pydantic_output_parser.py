from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
load_dotenv()

llm = HuggingFaceEndpoint(
     repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
)
model = ChatHuggingFace(llm=llm,temperature=0)

#main task
# create a pydantic object that will works as schema for output parser
class Person(BaseModel):
    name: str = Field(description="The name of the fictional person")
    age: int = Field(gt=18, description="The age of the fictional person")
    city: str = Field(description="The city where the fictional person lives")

# create the pydantic output parser my pydantic object is person class object
parser = PydanticOutputParser(pydantic_object=Person)
 
template = PromptTemplate(
    template="give me the name, age and city of a fictional {place} person\n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt = template.invoke({"place": "Italian"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print("Parsed Output:", final_result)