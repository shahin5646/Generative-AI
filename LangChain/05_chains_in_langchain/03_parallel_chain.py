from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model_01 = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)

model_02 = ChatGroq(
    model="qwen/qwen3.6-27b",
    temperature=0.7,  # low temp -> deterministic extraction, not creative generation
    max_tokens=1024,
)

prompt_01 = PromptTemplate(
    template="Generate a short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt_02 = PromptTemplate(
    template='Generate 5 questions answer from the text like a quiz \n {text}',
    input_variables=['text']   
)

prompt_03 =PromptTemplate(
    template='merge the provided document into a single document \n notes ->{notes}, quiz ->{quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt_01 | model_01 | parser,
    'quiz': prompt_02 | model_02 | parser,
})

merge_chain = prompt_03 | model_01 | parser

chain = parallel_chain | merge_chain

text = """
RunnableParallel
Runnable that runs a mapping of Runnables in parallel.

Returns a mapping of their outputs.

RunnableParallel is one of the two main composition primitives, alongside RunnableSequence. It invokes Runnables concurrently, providing the same input to each.

A RunnableParallel can be instantiated directly or by using a dict literal within a sequence.

Here is a simple example that uses functions to illustrate the use of RunnableParallel:

from langchain_core.runnables import RunnableLambda

def add_one(x: int) -> int:
    return x + 1

def mul_two(x: int) -> int:
    return x * 2

def mul_three(x: int) -> int:
    return x * 3

runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)
runnable_3 = RunnableLambda(mul_three)

sequence = runnable_1 | {  # this dict is coerced to a RunnableParallel
    "mul_two": runnable_2,
    "mul_three": runnable_3,
}
# Or equivalently:
# sequence = runnable_1 | RunnableParallel(
#     {"mul_two": runnable_2, "mul_three": runnable_3}
# )
# Also equivalently:
# sequence = runnable_1 | RunnableParallel(
#     mul_two=runnable_2,
#     mul_three=runnable_3,
# )

sequence.invoke(1)
await sequence.ainvoke(1)

sequence.batch([1, 2, 3])
await sequence.abatch([1, 2, 3])
RunnableParallel makes it easy to run Runnables in parallel. In the below example, we simultaneously stream output from two different Runnable objects:

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI

model = ChatOpenAI()
joke_chain = (
    ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
)
poem_chain = (
    ChatPromptTemplate.from_template("write a 2-line poem about {topic}")
    | model
)

runnable = RunnableParallel(joke=joke_chain, poem=poem_chain)

# Display stream
output = {key: "" for key, _ in runnable.output_schema()}
for chunk in runnable.stream({"topic": "bear"}):
    for key in chunk:
        output[key] = output[key] + chunk[key].content
    print(output)  # noqa: T201
RunnableParallel(
  self,
  steps__: Mapping[str, Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]]] | None = None,
  **kwargs: Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]] = {}
)
Bases
RunnableSerializable[Input, dict[str, Any]]
Used in Docs
Google cloud Vertex AI reranker integration
Parameters
Name	Type	Description
steps__	Mapping[str, Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]]] | None	
Default:
None
The steps to include.

**kwargs	Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]]	
Default:
{}
Additional steps to include.

Constructors
constructor
__init__
Name	Type
steps__	Mapping[str, Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]]] | None
Attributes
attribute
steps__
: Mapping[str, Runnable[Input, Any]]
attribute
model_config
attribute
InputType
: Any
The type of the input to the Runnable.

attribute
config_specs
: list[ConfigurableFieldSpec]
Get the config specs of the Runnable.

Methods
method
is_lc_serializable
Return True as this class is serializable.

method
get_lc_namespace
Get the namespace of the LangChain object.

method
get_name
Get the name of the Runnable.

method
get_input_schema
Get the input schema of the Runnable.

method
get_output_schema
Get the output schema of the Runnable.

method
get_graph
Get the graph representation of the Runnable.

method
invoke
method
ainvoke
method
transform
method
stream
method
atransform
method
astream
Inherited from
RunnableSerializable
Attributes
A
name
: str | None
—
The name of the Runnable.

Methods
M
to_json
—
Serialize the Runnable to JSON.

M
configurable_fields
—
Configure particular Runnable fields at runtime.

M
configurable_alternatives
—
Configure alternatives for Runnable objects that can be set at runtime.

Inherited from
Serializable
Attributes
A
lc_secrets
: dict[str, str]
—
A map of constructor argument names to secret ids.

A
lc_attributes
: dict[str, Any]
—
List of attribute names that should be included in the serialized kwargs.

Methods
M
lc_id
—
Return a unique identifier for this class for serialization purposes.

M
to_json
—
Serialize the object to JSON.

M
to_json_not_implemented
—
Serialize a "not implemented" object.

Inherited from
Runnable

"""


result = chain.invoke({'text':text})

# print(result)

chain.get_graph().print_ascii()