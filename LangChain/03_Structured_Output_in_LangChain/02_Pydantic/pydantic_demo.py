# Basic Structurs of Pydentic
# we need to install pydentic First

from pydantic import BaseModel , EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name: str
    # we can use optional, value jodi set na kora hoy tahole None return korbe.
    # Because LLMs extract information from text, and the information may not exist in the text.
    age: Optional[int] = None
    # We can add a email built in Validations
    email: EmailStr
    # we can use constrain[amra chaile jkuno value er range set korte pari ba condition kind of range apply korte pari]
    cgpa: float = Field(
        gt=0,
        lt= 4.1, 
        default=3.74, 
        description='A decimal Value representing the cgpa of a Student')
    
 
    
new_student = {
    "name": "Shahin",
    "age": 26,
    "email": "abcd@gmail.com",
    "cgpa": 4.00,
}


# creating student class object
student = Student(**new_student)

# converting a dictionaries
student_dict = student.model_dump()

# Converting json
student_json = student.model_dump_json()


# print(student_dict['age'])

print(student_json)


