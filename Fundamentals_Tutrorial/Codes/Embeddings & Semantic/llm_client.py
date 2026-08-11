import os

import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv
load_dotenv()

provider = "gemini"

def get_llm_response(message):
    if provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=message
        )
        return response.choices[0].message.content
    elif provider == "gemini":
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = ""

        for m in message:
            role = m["role"]
            content = m['content']
            prompt += f"{role}: {content}\n"

        response = model.generate_content(prompt)
        return response.text
    else:
        raise ValueError("Invalid PROVIDER. Use 'openai' or 'gemini'")