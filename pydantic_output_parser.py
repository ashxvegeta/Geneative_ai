from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# IMPORTANT: conversational task
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="conversational",
    temperature=0,
    max_new_tokens=200,
)

chat_model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str
    age: int = Field(gt=18)
    city: str

parser = PydanticOutputParser(pydantic_object=Person)

prompt = PromptTemplate(
    template=(
        "Give the name, age, and city of a fictional {place} person.\n"
        "{format_instructions}"
    ),
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

final_prompt = prompt.invoke({"place": "Italian"})

# 🔥 DO NOT use to_string()
response = chat_model.invoke(final_prompt)

result = parser.parse_with_prompt(
    response.content,
    final_prompt
)

print(result)
