import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))
prompt = "Explain transformers with a beginner friendly short explanation."

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt,
    max_output_tokens=250
)

print(f"User: {prompt}")
print(f"Model's Response: {response.output_text.strip()}")