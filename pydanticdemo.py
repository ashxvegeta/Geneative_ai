from  pydantic import BaseModel

class Student(BaseModel):
    name: str = "John Doe"
   
# Creating raw input data (dictionary)
new_student = {}

# Creating a Student object from the dictionary
Student = Student(**new_student)
print(Student.name)  # Output: John Doe


# ste default value in pydantic 
# from  pydantic import BaseModel

# class Student(BaseModel):
#     name: str = "John Doe"
   
# # Creating raw input data (dictionary)
# new_student = {}

# # Creating a Student object from the dictionary
# Student = Student(**new_student)
# print(Student.name)  # Output: John Doe
