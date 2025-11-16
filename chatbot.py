from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
while True:
    user_input  = input('You: ')
    if user_input == 'exit':
        break
    response = model.invoke(user_input)
    print("Bot:", response.content)