from llm_client import get_llm_response

print("===== Basic Chatbot (No External Knowledge)")
print("Type 'exit' to quit\n")

system_prompt = """
You are a helpful assistant.
If you do not know the answer for any question, still give it a try.
"""

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    message = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    response = get_llm_response(message)

    print(f"Bot: {response}")
    print("-"*30, "\n\n")