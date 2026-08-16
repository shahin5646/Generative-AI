# Without using strpuser

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)


prompt_template_01 = PromptTemplate(
    
    template="Write a detailed report on {topic}",
    input_variables=['topic']
    
)

# Template 02
prompt_template_02 = PromptTemplate(
    template="Write a 5 line summary on {text}",
    input_variables=['text']
)

# result
prompt1 = prompt_template_01.invoke({'topic':'Black Hole'})
result = model.invoke(prompt1)
# print(result.content)


prompt2 = prompt_template_02.invoke({'text':result.content})
result02 = model.invoke(prompt2)
print(result02.content)