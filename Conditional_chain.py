from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal 
load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback text")

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="classify the sentiment of the following feedback text into positive or negative\n{feedback}\n{format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)
chassifer_chain = prompt1 | model | parser2
# result = chassifer_chain.invoke({"feedback": "The product is wonderful and I am satisfied with the quality."}).sentiment
# print("Result:", result)

prompt2 = PromptTemplate(
    template="write an appropriate response to this positive feedback text\n{feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="write an appropriate response to this negative feedback text\n{feedback}",
    input_variables=["feedback"]
)
# branch_chain 
branch_chain = RunnableBranch(
    # if
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    # else if
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    #  else
    RunnableLambda(lambda x: "Could not classify the feedback sentiment")
)
# merging the chassifer_chain and branch_chain using RunnableParallel
final_chain = chassifer_chain | branch_chain
result = final_chain.invoke({"feedback": "The product is terrible and I am not satisfied with the quality."})
print("Final Result:", result)