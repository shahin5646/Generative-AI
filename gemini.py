import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = "Give a user friendly explanation of GenAI under 300 words"
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print(f"User: {prompt}")
print(f"Model Response: {response.text}")