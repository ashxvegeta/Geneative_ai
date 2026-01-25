
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import ResponseSchema, StructuredOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
)
model = ChatHuggingFace(llm=llm,temperature=0)

schemas = [
    ResponseSchema(name="fact1", description="fact 1 about the topic"),
    ResponseSchema(name="fact2", description="fact 2 about the topic"),
    ResponseSchema(name="fact3", description="fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)

templete= PromptTemplate(
    template="give me 3 facts about {topic} in the following format\n {fomat_instructions}" ,
    input_variables=["topic"],
    partial_variables={"fomat_instructions": parser.get_format_instructions()}
)

chain = templete | model | parser

result = chain.invoke({"topic": "climate change"})

print("Final Result:", result)