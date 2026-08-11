import warnings
warnings.filterwarnings("ignore")
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
result = model.invoke("What is the capital of Uganda")

print(result.text)