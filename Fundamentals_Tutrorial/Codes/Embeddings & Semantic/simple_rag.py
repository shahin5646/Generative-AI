from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from llm_client import get_llm_response
import numpy as np

print("=== Simple RAG Chatbot ===")
print("Type 'exit' to quit.\n")


# Step1: Internal Knowledge Base
documents = [
    "Company policy states that employees get 20 days of paid leave.",
    "Vikash is a Senior Data Scientist working in the AI team.",
    "The company follows a hybrid work model with 3 days in office.",
    "Employees receive health insurance and performance bonuses."
]


# Step2: Create Embeddings
vectorizer = TfidfVectorizer()
doc_embeddings = vectorizer.fit_transform(documents)

# Step3: Retrieval Function
def retrieve(query, top_k=2):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, doc_embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]

    print("===== Printing variables as logs for debugging =====")
    print(f"Cosine similarity return:\n{cosine_similarity(query_vec, doc_embeddings)}")
    print(f"Cosine similarity with [0]:\n{cosine_similarity(query_vec, doc_embeddings)[0]}")
    print(f"np argsort return value: {np.argsort(similarities)}")
    print(f"np argsort [::-1] value: {np.argsort(similarities)[::-1]}")
    print(f"np argsort [:top_k] value: {np.argsort(similarities)[::-1][:top_k]}")
    print("=======================================================")



    return [documents[i] for i in top_indices]


# Step4: Chat loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    retrieved_docs = retrieve(user_input)
    context = "\n".join(retrieved_docs)

    # Step5: Augmented Prompt
    message = [
        {
            "role": "system",
            "content": "Anwer ONLY using the provided context. If not found, say 'I dont know.'"
        },
        {
            "role": "user",
            "content": f"""
Context:
{context}

Question:
{user_input}
"""
        }
    ]

    response = get_llm_response(message)
    # print("\n Retrieved Context: ")
    # for doc in retrieved_docs:
    #     print("-", doc)

    print(f"Bot's Response: {response}\n\n")