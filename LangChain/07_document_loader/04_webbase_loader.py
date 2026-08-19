from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Web base Loader
url = 'https://dazzle.com.bd/product/apple-macbook-pro-m5-14-inch-10-core-cpu-10-core-gpu-price-in-bangladesh'

loader = WebBaseLoader(url)

docs = loader.load()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)

# prompt
prompt = PromptTemplate(
    template='Answer following question - \n {questions} from the following text - \n {text}',
    input_variables=['questions', 'text'],
)

# parser
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    'questions':'what are the cpu performance and gpu cores ?',
    'text' : docs[0].page_content,
})

print(result)