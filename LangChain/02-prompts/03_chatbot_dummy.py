from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    max_tokens=1024,
)


'''

while True:
    user_input = input('User: ')
    if user_input == 'exit':
        break
    result = model.invoke(user_input)
    print("AI: ",result.content)

In this format AI loose chat history.it can not remeber what we asked previously
'''


'''

chat_history = []
while True:
    user_input = input('User: ')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)
    
print(chat_history)

In this method there is a problem.Chat barar sathe sathe user history te confusion aste thakee. AI er jonno buja tough kunta user bolche r kunta ai.

LANGCHAIN SOLVES THIS PROBLEM VIA MESSAGES TYPE. 
3 TYPES:
    1. System message
    2.Human Message
    3. AI message
'''
chat_history = [
    SystemMessage(content='You are a helpful assistant!')
]


while True:
    user_input = input('User: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)