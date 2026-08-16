#  using strpuser commonly used in chains

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)


prompt_template_01 = PromptTemplate(
    
    template="Write a detailed report on {topic}",
    input_variables=['topic']
    
)

# Template 02
prompt_template_02 = PromptTemplate(
    template="Write a 5 line summary on {text}",
    input_variables=['text']
)

parser = StrOutputParser()

# creating a chain

chain = prompt_template_01 | model | parser | prompt_template_02 | model | parser

result = chain.invoke({'topic':'Black Hole'})

print(result)


