# tell a joke and explain it using Runnable sequence
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2, 
    max_tokens=1024,
)

# prompt 1
prompt_01 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# prompt 02
prompt_02 = PromptTemplate(
    template='Explain the {text}',
    input_variables=['text']
)

# parser
parser = StrOutputParser()

# chain
chain = RunnableSequence(prompt_01, model, parser, prompt_02, model, parser)

# result
result = chain.invoke({'topic':'AI'})
print(result)

'''
We send {'topic': 'AI'} into prompt_01 first because it's first in the sequence. Everything after that just passes along whatever string came out of the step before it. prompt_02 automatically wraps that incoming string into a dict for its one variable (text) — but only because it has exactly one variable. If it had two, there'd be no way to know which one the string belongs to, so it crashes instead of guessing.
'''
