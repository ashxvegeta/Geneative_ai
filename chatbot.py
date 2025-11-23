from langchain_openai import ChatOpenAI
# import message types
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
# create an empty chat history list and add system message
chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
] 
while True:
    user_input  = input('You: ')
    # append user input to chat history and make a human message
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    # get model response based on chat history
    response = model.invoke(chat_history)
    # append model response to chat history and make ai message
    chat_history.append(AIMessage(content=response.content))
    
    print("Bot:", response.content)

print(chat_history)