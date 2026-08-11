'''
Project: Find which document answers a user's question

We have 5 documents. User asks a question. We have to find out
which document the answer is most likely coming from.

Steps:
    1. Generate embedded vectors for all 5 documents.
       ** All vectors are same dimensions [we assume]
    2. Generate embedded vector for the user's question.
    3. Compare the question vector against all 5 document vectors
       using cosine similarity.
    4. The document with the highest similarity score = our answer.
'''

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about ms dhoni'

# NOTE: every time we run this, we're generating fresh embeddings for all
# 5 documents again — nothing is being stored anywhere. That's costly.
# Once we learn vector DBs, we'll embed documents ONCE and store them,
# so we only need to embed the incoming query each time.
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# cosine_similarity() expects 2D input for both arguments.
# doc_embeddings is already 2D (list of vectors), but query_embedding
# is a single 1D vector — so we wrap it in [ ] to make it 2D too.
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Pair each score with its document index, sort by score,
# and take the last one = highest similarity = best match.
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print('Similarity score: ', score)