
from typing import TypedDict ,Literal,Annotated,Optional

class Person(TypedDict):
    name: str
    age: int
    
new_person: Person ={
    'name': 'Shahin',
    'age' : 25
}

print(new_person)

