from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

#take a input and make a list of messages kind of chat history
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, who won the world series in 2020?"),
]
# send the messages to the model
response = model.invoke(messages)
# extact the message given by the model and make a ai message and append to messages
messages.append(AIMessage(content=response.content))
print(messages)
