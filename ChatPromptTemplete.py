from langchain_core.prompts  import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

chat_templete = ChatPromptTemplate.from_messages( [
    SystemMessage(content="You are a helpful {domain} expert."),
    HumanMessage(content=" Explain the concept of {concept} in simple terms."),
])

prompt = chat_templete.invoke(
    {
        "domain": "physics",
        "concept": "quantum mechanics"
    }
)   
print(prompt)

# Output:
# now in this ocode there is a problem that the variables are not replaced with their values
# so the output will be like below
# messages=[SystemMessage(content='You are a helpful {domain} expert.', additional_kwargs={}, response_metadata={}), HumanMessage(content=' Explain the concept of {concept} in simple terms.', additional_kwargs={}, response_metadata={})]