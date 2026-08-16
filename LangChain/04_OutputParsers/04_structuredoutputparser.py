from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv


load_dotenv()

#  Problem with StructuredOutputParser we can not do data validation with that like we can not decide name should be str ,age integer 

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)

schema = [
    ResponseSchema(name='fact_1',description='Fact 1 about the topic.'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic.'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic.'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me 3 facts about {topic} \n {format_instruction} ",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'blackhole'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template | model | parser
result = chain.invoke({'topic':'blackhole'})

print(result)