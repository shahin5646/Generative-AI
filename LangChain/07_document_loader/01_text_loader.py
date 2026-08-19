from langchain_community.document_loaders import TextLoader
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

# Text Loader
loader = TextLoader('story.txt', encoding= 'utf-8')
docs = loader.load()

# prompt
prompt = PromptTemplate(
    template='Write a summary of the story \n {story}',
    input_variables=['story'],
)

# parser
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'story':docs[0].page_content})
print(result)



