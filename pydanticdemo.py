from  pydantic import BaseModel

class Student(BaseModel):
    name: str
   
# Creating raw input data (dictionary)
new_student = {'name': 32}

# Creating a Student object from the dictionary
Student = Student(**new_student)
print(Student)  # Output: John Doe