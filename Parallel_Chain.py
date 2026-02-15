from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1 = ChatOpenAI(model="gpt-4o-mini", temperature=0)
model2 = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt1 = PromptTemplate(
    template="Generate a short and simple notes from the following text \n {text}",
    input_variables=["text"]
)
prompt2 = PromptTemplate(
    template="Generate 5 short question and answers from the following text \n {text}",
    input_variables=["text"]
)
prompt3 = PromptTemplate(
    template="Merge the provided  notes and  quiz into a single text \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes", "quiz"]
)
parser = StrOutputParser()
parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser,
})
merge_chain = prompt3 | model1 | parser
final_chain = parallel_chain | merge_chain
text = """Sarvam Ai is an initiative by the Government of India to 
promote the development and adoption of artificial intelligence (AI) 
technologies in the country. The initiative aims to create a conducive ecosystem 
for AI research, development, and deployment across various sectors, including healthcare, 
agriculture, education, and smart cities. Sarvam Ai focuses on fostering innovation, building AI 
capabilities,and ensuring ethical and responsible use of AI in India."""
final_result = final_chain.invoke({"text": text})
print("Final Result:", final_result)