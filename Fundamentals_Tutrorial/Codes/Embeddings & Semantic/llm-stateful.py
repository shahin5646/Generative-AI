from llm_client import get_llm_response

print("--- Stateful Chatbot (With Memory)")
print("Type 'exit' to quit\n")


chat_history = []

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append({"role": "user", "content": user_input})

    MAX_HISTORY = 5

    response = get_llm_response(chat_history[-MAX_HISTORY:])
    print(f"Bot: {response}")

    chat_history.append({"role": "assistant", "content": response})