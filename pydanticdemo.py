from  pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
   
# Creating raw input data (dictionary)
# here u can see age is string but pydantic will convert it to int so this is called type coercion and in output age will be int
new_student = {"age": "20"}

# Creating a Student object from the dictionary
Student = Student(**new_student)
print(Student)  # Output: John Doe


