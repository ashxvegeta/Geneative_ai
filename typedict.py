# TypedDict helps by telling Python (and your IDE):

# “This dictionary must follow a specific structure.”
from typing import TypedDict

class person_info(TypedDict):
    name: str
    age: int
    

name_person = person_info(name='Alice', age=30)
print(name_person)  # Output: {'name': 'Alice', 'age': 30}