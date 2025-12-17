from  pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
   
# Creating raw input data (dictionary)
new_student = {}

# Creating a Student object from the dictionary
Student = Student(**new_student)
print(Student)  # Output: John Doe


