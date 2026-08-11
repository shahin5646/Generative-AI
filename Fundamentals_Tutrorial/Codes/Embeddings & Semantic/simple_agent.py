import json
from llm_client import get_llm_response
import random


print("===== Multi-Tool AI Agent =====")
print("Type 'exit' to quit\n")


# Tools
def get_weather(city):
    weather_opt = [f"The weather in {city} is 35*c and sunny.", f"The weather in {city} is 16*c and pleasant."]
    final = random.choice(weather_opt)
    return final

def suggest_activity(weather):
    if "hot" in weather.lower() or "35" in weather:
        return "Stay indoors, do yoga or light streatching."
    else:
        return "Go for a run or outdoor walk."
    
def calorie_estimator(activity):
    if "yoga" in activity.lower():
        return "Estimated calories burned: 150 kcal"
    elif "run" in activity.lower():
        return "Estimated calories burned: 300 kcal"
    else:
        return "Estimated calories burned: 50 kcal"
    

TOOLS = {
    "weather": get_weather,
    "activity": suggest_activity,
    "calories": calorie_estimator
}


SYSTEM_PROMPT = """
You are an intelligent planning agent.

You must solve the user's problem step-by-step using tools.

Available Tools:
1. weather(city)
2. activity(weather)
3. calories(activity)

Rules:
- Think step-by-step
- Use tools when needed
- You can call multiple tools in sequence
- Use previous results to decide next step

Respond ONLY in JSON:

Step format:
{
  "action": "tool_name",
  "input": "input"
}

Final format:
{
  "final_answer": "complete answer"
}

Do NOT use markdown.
"""

# Agent Loop:
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    context = user_input
    step = 1

    while True:
        print(f"\n----- Step: {step} -----")

        message = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context}
        ]

        response = get_llm_response(message)
        print(f"\nAgent Decision: {response}")

        clean = response.replace("```json", "").replace("```", "").strip()

        try:
            data = json.loads(clean)
            if "final_answer" in data:
                print(f"\nFinal Plan:\n{data['final_answer']}\n")
                break

            # tool calling
            action = data.get("action")
            tool_input = data.get("input", "")

            if action in TOOLS:
                print(f"Using tool: {action} with input: {tool_input}")

                result = TOOLS[action](tool_input)
                print(f"Observation via tool: {result}")

                context += f"\nResult of {action}: {result}"
            else:
                print("Unknown tool!!\n\n")
                break

        except:
            print("Failed to parse response!!\n\n")
            break

        step += 1