import os
from llama_index.llms import Replicate
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index import ServiceContext
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Create the 'data' folder
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

# Create a text file with the specified content
text_content = "The value is 123ABC"
text_file_path = os.path.join(data_folder, "document.txt")
with open(text_file_path, "w") as file:
    file.write(text_content)

os.environ["REPLICATE_API_TOKEN"] = "r8_C5coib4oOsxp8WfYWfQ64Ipmh21JX4n0uQ9mz"

llama2_7b_chat = "meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e"
llm = Replicate(
    model=llama2_7b_chat,
    temperature=0.01,
    additional_kwargs={"top_p": 1, "max_new_tokens":300}
)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents, service_context=service_context)
query_engine = index.as_query_engine()
query_result = query_engine.query("What is the value?")

print("Query Result:", query_result)

# Clean up: Delete the 'data' folder
import shutil
shutil.rmtree(data_folder)
