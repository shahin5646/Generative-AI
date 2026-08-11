'''
Project: Find which document answers a user's question
---------------------------------------------------------
We have 5 documents. User asks a question. We have to find out
which document the answer is most likely coming from.

Steps:
    1. Generate embedded vectors for all 5 documents.
       ** All vectors are same dimensions [we assume]
    2. Generate embedded vector for the user's question.
    3. Compare the question vector against all 5 document vectors
       using cosine similarity.
    4. The document with the highest similarity score = our answer.

This version runs fully locally using Hugging Face + sentence-transformers.
No API key needed, no per-call cost — but quality is generally lower
than OpenAI's text-embedding-3-large, and dimension size is fixed
(MiniLM doesn't support a `dimensions` shortening parameter).
'''

import os
os.environ['HF_HOME'] = 'E:/huggingface_cache'

from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about ms dhoni'

# NOTE: same limitation as the OpenAI version — every run recomputes
# embeddings for all 5 documents from scratch. Nothing is cached/stored.
# Once we learn vector DBs, we'll embed documents ONCE and store them.
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

# cosine_similarity() needs 2D input for both args — doc_embeddings is
# already 2D, query_embedding is 1D so we wrap it in [ ] to match.
scores = cosine_similarity([query_embedding], doc_embeddings)[0]

# Pair each score with its document index, sort by score,
# take the last one = highest similarity = best match.
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print('Similarity score: ', score)


