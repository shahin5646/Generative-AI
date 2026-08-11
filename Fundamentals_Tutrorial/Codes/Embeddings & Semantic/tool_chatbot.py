import json
from llm_client import get_llm_response
from datetime import datetime

print("===== Tool-enabled Chatbot =====")
print("Type 'exit' to quit\n")

# Step1: Define Tools

def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid calculation"
    
def get_weather(city):
    # mock weather data
    return f"The weather in {city} is 16*c and sunny."

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Tool Registry
TOOLS = {
    "calculator": calculator,
    "weather": get_weather,
    "time": get_current_time
}

# Step2: System Prompt (Important)
SYSTEM_PROMPT = """
You are an AI assistant with access to tools.

Available tools:
1. calculator -> for math expressions
2. weather -> for city weather
3. time -> for current time

When a tool is needed, response ONLY in this JSON format:

{
  "tool": "tool_name",
  "input": "input_for_tool"
}

If no tool is needed, response normally.
"""

# Step3: Chat Loop
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    message = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ]

    response = get_llm_response(message)
    print(f"\nRaw Response: {response}")

    clean = response.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(clean)

        tool = data["tool"]
        tool_input = data.get("input", "")

        if tool in TOOLS:
            print(f"\nUsing tool: {tool}")

            result = TOOLS[tool](tool_input) if tool_input else TOOLS[tool]()
            print(f"Tool output: {result}")

            # Ask LLM to generate final answer
            final = get_llm_response([
                {"role": "user", "content": f"User asked: {user_input}\n Tool result: {result}"}
            ])

            print(f"Bot's Final Answer: {final}")
        else:
            print(f"Bot's Answer: {response}")
    except:
        print(f"Bot's Answer: {response}")