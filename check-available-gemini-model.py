import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

models = client.models.list()

for m in models:
    if "generateContent" in getattr(m, "supported_actions", []):
        print(f"Valid: {m.name}")
    else:
        print(f"Skip: {m.name} | Supports: {getattr(m, 'supported_actions', None)}")