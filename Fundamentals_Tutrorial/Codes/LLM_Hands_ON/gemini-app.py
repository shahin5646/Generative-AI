import os
from dotenv import load_dotenv

# must be set BEFORE importing google.generativeai
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "3"  # 3 = FATAL only
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

prompt = "Give a beginner friendly explaiantion of LLMs under 200 words."

response = model.generate_content(prompt)

print(f"User: {prompt}")
print(f"Model's Response: {response.text}")