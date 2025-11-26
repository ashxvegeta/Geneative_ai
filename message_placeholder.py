from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# chat templete
chat_templete = ChatPromptTemplate( [
    ('system', 'You are a helpful customer support agent.'),
    # all the conversation history will be stored in chat_history variable between user and 
    # customer support agent so that human message have all the context of  previous chats
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])
# creat a chat history list
chat_history = []
# load chat hitory
with open('chat_history.txt',) as f:
    # will read entire file content form text file  and append it in  chat_history list
    for line in f:
        chat_history.append(line.strip())
print(chat_history)
# create prompt
# now we can pass the chat_history variable to the prompt template and query variable
prompt = chat_templete.invoke({'chat_history': chat_history,'query': 'where is my refund'})
print(prompt)

# now the llm have whole context of previous chat history between human and customer support agent
# and also the current query of human so that it can give better response
# ['HumanMessage(content="I want to request a refund for my order #12345.")', 'AIMessage(content="Your refund request for order #12345 has been initiated. It will be', 'processed in 3-5 business days.")']
# messages=[SystemMessage(content='You are a helpful customer support agent.', additional_kwargs={}, response_metadata={}), HumanMessage(content='HumanMessage(content="I want to request a refund for my order #12345.")', additional_kwargs={}, response_metadata={}), HumanMessage(content='AIMessage(content="Your refund request for order #12345 has been initiated. It will be', additional_kwargs={}, response_metadata={}), HumanMessage(content='processed in 3-5 business days.")', additional_kwargs={}, response_metadata={}), HumanMessage(content='where is my refund', additional_kwargs={}, response_metadata={})]