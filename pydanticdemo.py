from  pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: Optional[float] = Field(gt=0, lt=10)  # cgpa must be between 0 and 10

# Creating raw input data (dictionary)
# here i have put wrong email format to show validation
new_student = {"age": "20" , "email": "ashu@gmail.com", "cgpa": 11.5}

# Creating a Student object from the dictionary
Student = Student(**new_student)
print(Student)  # Output: John Doe


