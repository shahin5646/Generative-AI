# Customer provide us a feedback.we have to anlayze the sentiment.based on the review we should provide feedback .if positive provide positive response and if negative reply convanient message based on the problem

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  
    max_tokens=1024,
)

class Feedback(BaseModel):
    
    sentiment: Literal['positive','negative'] = Field(
        description='Give me the sentiment of the review of the feedback'
    )

parser = StrOutputParser()
parser_02 = PydanticOutputParser(pydantic_object= Feedback)
prompt_01 = PromptTemplate(
    template='classify the following feedback text positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser_02.get_format_instructions()}
)

classifier_chain = prompt_01 | model | parser_02

prompt_02 = PromptTemplate(
    template='Give a appropriate response for this positive response \n {feedback}',
    input_variables=['feedback']
)
prompt_03 = PromptTemplate(
    template='Give a appropriate response for this negative response \n {feedback}',
    input_variables=['feedback']
)

branch_chain =RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt_02 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt_03 | model | parser),
    RunnableLambda(lambda x: 'could not find any sentiment')
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback':'its a terrible smartphone'}))

