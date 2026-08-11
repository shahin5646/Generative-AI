from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)
result = embedding.embed_query('Dhaka is the most crowded city in Bangladesh')

print(str(result))
