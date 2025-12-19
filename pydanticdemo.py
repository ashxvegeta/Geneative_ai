from  pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name: str = "John Doe"
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: Optional[float] = Field(gt=0, lt=10,default=5,description="CGPA must be between 0 and 10")  # cgpa must be between 0 and 10

# Creating raw input data (dictionary)
# here i have put wrong email format to show validation
new_student = {"age": "20" , "email": "ashu@gmail.com"}

# Creating a Student object from the dictionary
Student = Student(**new_student)

# converting the Student object back to a dictionary
Student_json = Student.model_dump_json()
print(Student_json)  
