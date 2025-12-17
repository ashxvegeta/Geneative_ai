from  pydantic import BaseModel,EmailStr
from typing import Optional
class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    email: Optional[EmailStr] = None
   
# Creating raw input data (dictionary)
# here i have put wrong email format to show validation
new_student = {"age": "20" , "email": "ss.com"}

# Creating a Student object from the dictionary
Student = Student(**new_student)
print(Student)  # Output: John Doe


