from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are an Expert in {domain}'),
    ('human', 'Explain in simple terms, beginner friendly, about what is {topic}?'),
])

prompt = chat_template.invoke(
    {
        'domain':'cricket',
        'topic' : 'timeout'
    }
)

print(prompt)