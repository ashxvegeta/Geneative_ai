from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# detaild report prompt
templete1= PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic'])

# 5 line summery prompt with output parser
templete2= PromptTemplate(
    template='write a 5 line summery on the following text./n {text}',
    input_variables=['text'])


parser = StrOutputParser()

# my pipeline chain
chain = templete1 | model | parser |  templete2 | model | parser
result = chain.invoke({"topic": "climate change"})
print(result)

