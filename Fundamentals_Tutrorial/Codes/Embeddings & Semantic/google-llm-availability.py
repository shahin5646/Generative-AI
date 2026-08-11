import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

for m in models:
    if "generateContent" in getattr(m, "supported_generation_methods", []):
        print(f"Valid: {m.name}")
    else:
        print(f"Skip: {m.name} | Supports: {getattr(m, 'supported_generation_methods', None)}")
    
    # if "generateContent" in getattr(m, "supported_generation_methods", []):
    #     print("VALID:", m.name)
    # else:
    #     print("SKIP:", m.name, "-> supports:", getattr(m, "supported_generation_methods", None))