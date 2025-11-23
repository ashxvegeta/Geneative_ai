from langchain_core.prompts  import ChatPromptTemplate

# we can use this way also to create chat prompt template
# chat_templete = ChatPromptTemplate.from_messages([
#     ('system', 'You are a helpful {domain} expert.'),
#     ('human', ' Explain the concept of {concept} in simple terms.')
# ])
chat_templete = ChatPromptTemplate( [
    ('system', 'You are a helpful {domain} expert.'),
    ('human', ' Explain the concept of {concept} in simple terms.')
])

prompt = chat_templete.invoke(
    {
        "domain": "physics",
        "concept": "quantum mechanics"
    }
)   
print(prompt)
