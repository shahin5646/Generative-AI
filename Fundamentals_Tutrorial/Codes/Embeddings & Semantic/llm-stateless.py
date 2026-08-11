import warnings
warnings.filterwarnings('ignore')

from llm_client import get_llm_response

print("--- Stateless Chatbot (No Memory)")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages = [
        {"role": "user", "content": user_input}
    ]

    response = get_llm_response(messages)
    print(f"Bot: {response}")