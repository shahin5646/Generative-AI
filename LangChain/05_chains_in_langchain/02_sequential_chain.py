from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


# a sequential chain that take a input and make summary of the topic from the input

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)


prompt_01 = PromptTemplate(
    template='Generate a Detailed report on {topic}',
    input_variables=['topic']
    
)
prompt_02 = PromptTemplate(
    template='Generate a five point summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt_01 | model | parser | prompt_02 | model | parser

result = chain.invoke({'topic':'Sylhet travel Places'})

# print(result)

# Graph 
chain.get_graph().print_ascii()

