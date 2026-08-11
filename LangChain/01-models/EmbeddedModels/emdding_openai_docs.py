from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    'Dhaka is the Capital of Bangladesh',
    'Sylhet is one of the most beautiful city in Bangladesh',
    'This is a beautiful Place to visit'
]

result = embedding.embed_documents(documents)

print(str(result))