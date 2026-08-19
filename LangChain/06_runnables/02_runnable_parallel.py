# from two models ,one should generate tweet and linkedIn post using runnable seqience .It produces a dictionary of output
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# model
model_01 = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.2, 
    max_tokens=1024,
)
# model 02
model_02 = ChatGroq(
    model="qwen/qwen3.6-27b",
    temperature=0.2, 
    max_tokens=1024,
)

# prompt01
prompt_01 = PromptTemplate(
    template='Generate a tweet post about {topic}',
    input_variables=['topic']
)

# prompt 02
prompt_02 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

# parser
parser = StrOutputParser()

# parallel runnable
chain = RunnableParallel({
    'tweet':RunnableSequence(prompt_01, model_01, parser),
    'linkedIn': RunnableSequence(prompt_02, model_02, parser)
})

# result
result = chain.invoke({'topic':'GenAI'})

print(result)