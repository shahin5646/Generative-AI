'''
RunnableLambda is a runnable primitive that allows you to apply custom Python functions
within an Al pipeline.
It acts as a middleware between different Al components, enabling preprocessing,
transformation, API calls, filtering, and post-processing in a LangChain workflow.
'''

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence ,RunnableParallel, RunnablePassthrough , RunnableLambda
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


# model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7, 
    max_tokens=1024,
)

# word count function
def wordCount(text):
    return len(text.split())
# prompt
prompt = PromptTemplate(
    template='tell a joke about {topic}',
    input_variables=['topic']
)

# parser
parser = StrOutputParser()

# joke generator
joke_generate_chain = prompt | model | parser

# parallel chain
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(wordCount)
})

final_chain = joke_generate_chain | parallel_chain

result = final_chain.invoke({'topic':'Film Industry'})


print(result)
