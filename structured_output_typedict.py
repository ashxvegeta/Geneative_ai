from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()

model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# schema for structured output using TypedDict

class Review(TypedDict):
   summary: str
   sentiment: str

# create a structured model with the Review schema
structured_model = model.with_structured_output(Review)

# invoke the model with a product review
result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")

print(result)
# Output will be a dictionary following the Review schema

# u can access individual fields
print("Summary:", result['summary'])
print("Sentiment:", result['sentiment'])