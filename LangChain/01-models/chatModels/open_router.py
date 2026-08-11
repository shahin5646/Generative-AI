from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenRouter(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    reasoning={"enabled": True}
)

result = model.invoke("How many r's are in the word 'strawberry'?")
print(result.content)

# Second call — continue the conversation, preserving reasoning
messages = [
    ("human", "How many r's are in the word 'strawberry'?"),
    result,  # LangChain's AIMessage object — carries reasoning metadata automatically
    ("human", "Are you sure? Think carefully."),
]

result2 = model.invoke(messages)
print(result2.content)
