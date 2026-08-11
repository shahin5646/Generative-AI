import os
os.environ['HF_HOME'] = 'E:/huggingface_cache'

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name ='sentence-transformers/all-MiniLM-L6-v2')

# # Single line
# text = 'Dhaka is the capital of Bangladesh'

documents = [
    'Dhaka is the Capital of Bangladesh',
    'Sylhet is one of the most beautiful city in Bangladesh',
    'This is a beautiful Place to visit'
]


vector = embedding.embed_documents(documents)

print(str(vector))