from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


'''
Human Message : message sent by the user or user inputs.
AIMessage : Message from an AI.An AIMessage is returned from a chat model as a response to a prompt.
SystemMessage : Message for priming AI behavior.The system message is usually passed in as the first of a sequence of input messages.
Example:
        messages = [
            SystemMessage(content="You are a helpful assistant! Your name is Bob."),
            HumanMessage(content="What is your name?"),
        ]

'''


load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    max_tokens=1024,
)

messages = [
    SystemMessage(content='You are a helpful assistant!'),
    HumanMessage(content='What is LangChain ?'),
    
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)

