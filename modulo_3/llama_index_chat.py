import os
from llama_index.llms import Replicate
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index import ServiceContext, SimpleDirectoryReader, VectorStoreIndex


with open("../replicate_api_token.txt") as file:
    os.environ["REPLICATE_API_TOKEN"] = file.read(40)

llm = Replicate(
    model="meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e",
    temperature=0.01,
    additional_kwargs={"top_p": 1, "max_new_tokens": 1000}
)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

query_engine = index.as_query_engine()

while True:
    query = input("\nQUESTION: ") 
    query_result = query_engine.query(query)
    print(f"ANSWER:{query_result}")
