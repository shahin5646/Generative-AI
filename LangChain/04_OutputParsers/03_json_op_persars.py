from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

#  Problem with json parsing we can not enforce schema

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)

parser = JsonOutputParser()

template = PromptTemplate(
    # template="Give me a Imaginary name, age , city of a foctional person \n {format_instruction}",
    template="Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.format()
# # print(prompt)

# result = model.invoke(prompt)
# # print(result)

# final_result = parser.parse(result.content)


# we can use chain
chain = template | model | parser
result = chain.invoke({'topic':'blackholes'})
print(result)