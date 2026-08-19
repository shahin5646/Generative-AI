'''
RunnableBranch is a control flow component in LangChain that allows you to conditionally
route input data to different chains or runnables based on custom logic.
It functions like an if/elif/else block for chains — where you define a set of condition functions,
each associated with a runnable (e.g., LLM call, prompt chain, or tool). The first matching
condition is executed. If no condition matches, a default runnable is used (if provided).

specially used in conditional like if else

'''
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence ,RunnableParallel, RunnablePassthrough , RunnableLambda , RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


# model
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7, 
    max_tokens=3024,
)

# prompt --01
prompt_01 = PromptTemplate(
    template='write a detailed report on  {topic}',
    input_variables=['topic']
)
# prompt --02
prompt_02 = PromptTemplate(
    template='Summarize the following {text}',
    input_variables=['text']
)

# parser
parser = StrOutputParser()

# sequential chain
report_generator = prompt_01 | model | parser

# Branch chain
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500,  prompt_02 | model | parser),
    RunnablePassthrough()
)

final_chain = report_generator | branch_chain

result = final_chain.invoke({'topic':'USA vs Iran War'})
print(result)