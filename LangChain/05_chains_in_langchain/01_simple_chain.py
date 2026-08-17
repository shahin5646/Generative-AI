# creating a simple chain
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)

prompt = PromptTemplate(
    template='Generate five interesting facts about {topic} in short',
    input_variables= ['topic'],
)

parser = StrOutputParser()

chain = prompt | model  | parser

result = chain.invoke({'topic':'Tajmahal'})

# print(result)

# check chain graph
chain.get_graph().print_ascii()
