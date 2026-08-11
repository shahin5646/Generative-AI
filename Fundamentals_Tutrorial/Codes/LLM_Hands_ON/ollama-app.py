import ollama

prompt = "WHat is the currency of Japan?"

response = ollama.chat(
    model="mistral",
    messages=[{"role": "user", "content": prompt}]
)

print(response["message"]["content"].strip())