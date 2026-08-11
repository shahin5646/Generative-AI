import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
prompt = "Explain transformers with a beginner friendly short explanation."

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=250
)

print(f"User: {prompt}")
print(f"Model's Response: {response.choices[0].message.content.strip()}")