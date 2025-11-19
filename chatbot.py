from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
# create an empty chat history list
chat_history = [] 
while True:
    user_input  = input('You: ')
    # append user input to chat history
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    # get model response based on chat history
    response = model.invoke(chat_history)
    # append model response to chat history 
    chat_history.append(response.content)
    
    print("Bot:", response.content)

print(chat_history)