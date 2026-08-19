# RunnablePassthrough is a special Runnable primitive that simply returns the input as output
# without modifying it.

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence ,RunnableParallel, RunnablePassthrough , RunnableLambda
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2, 
    max_tokens=1024,
)

# prompt01
prompt_01 = PromptTemplate(
    template='tell a joke about {topic}',
    input_variables=['topic']
)

# prompt 02
prompt_02 = PromptTemplate(
    template='Explain the joke {text}',
    input_variables=['text']
)

# parser
parser = StrOutputParser()

# joke generator 
joke_generator_chain = prompt_01 | model | parser

# parallel runnable
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation': prompt_02 | model | parser
})

final_Chain = joke_generator_chain | parallel_chain

result = final_Chain.invoke({'topic':'football'})
print(result)