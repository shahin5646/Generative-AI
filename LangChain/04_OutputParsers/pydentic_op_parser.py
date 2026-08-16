from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)


class Person(BaseModel):
    name: str = Field(
        description="Name of the Person"
    )
    
    age: int =Field(
        gt = 18,
        description='Age of the Person'
    )
    
    city: str = Field(
        description='Name of the City the person live '
    )
    

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template= "Generate a fictional name ,age,city of a {nationality} person \n {format_instruction}",
    input_variables= ['nationality'],
    partial_variables= {'format_instruction':parser.get_format_instructions()}
)

'''
#WITHOUT CHAIN
prompt = template.invoke({'nationality':'Bangladeshi'})
result = model.invoke(prompt)

final_result = parser.parse(result.content)
print(final_result)

'''

chain = template | model | parser
final_result = chain.invoke({'nationality': 'Pakistani'})

print(final_result)