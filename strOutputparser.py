from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm,temperature=0)

# 1st prompt
templete1= PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic'])

templete2 = PromptTemplate(
    template=(
               "Return ONLY 5 bullet points.\n"
        "Each bullet must be ONE sentence.\n"
        "Do NOT add headings.\n"
        "Do NOT add numbers.\n"
        "Do NOT introduce new topics.\n"
        "Do NOT exceed 5 lines.\n\n"
        "{text}"

    ),
    input_variables=["text"]
)


prompt1 = templete1.invoke({"topic": "black holes"})
result1 = model.invoke(prompt1.to_messages())
prompt2 = templete2.invoke({"text": result1.content})
result2 = model.invoke(prompt2.to_messages())
print(result2.content)