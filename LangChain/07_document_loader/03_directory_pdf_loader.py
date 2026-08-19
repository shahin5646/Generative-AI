from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path= 'books',
    glob= '*.pdf',
    loader_cls= PyPDFLoader
)

docs = loader.lazy_load()

# print(docs[320].page_content)

for documents in docs:
    print(documents.metadata)