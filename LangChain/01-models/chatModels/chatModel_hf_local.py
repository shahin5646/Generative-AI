import os
os.environ['HF_HOME'] = 'E:/huggingface_cache'

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
        do_sample=True,
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke('What is the capital of Bangladesh?')

print(result.content)