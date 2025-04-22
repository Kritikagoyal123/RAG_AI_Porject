from http.client import responses

import chromadb
from llama_index.core import PromptTemplate, Settings, SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from chromadb import PersistentClient


# Initialize ChromaDB persistent client and collection
chroma_client1=chromadb.PersistentClient(path='./Quality_Alloys1_db')
chroma_collection= chroma_client1.get_or_create_collection('Quality_Alloys_col')

# Set the embedding model and LLM
embed_model=HuggingFaceEmbedding(model_name='BAAI/bge-small-en')
Settings.llm=Ollama(model="deepseek-r1:1.5b", request_timeout=360.0)
Settings.embed_model=embed_model

# Define a custom prompt template
custom_prompt = PromptTemplate(
    template="Provide a clear and concise answer to {query_str}."
)

# Set up the vector store and index from pre-existing data

#documents=SimpleDirectoryReader('./data/').load_data()
vector_store=ChromaVectorStore(chroma_collection=chroma_collection)
storage_context=StorageContext.from_defaults(vector_store=vector_store)
index= VectorStoreIndex.from_vector_store(vector_store,storage_context=storage_context)

# Run a query using the custom prompt and top_k setting
query_engine=index.as_query_engine(llm=Settings.llm ,similarity_top_k=1, text_qa_template=custom_prompt)
response=query_engine.query('Based on the data provided in the excel file, did the promotional brochure increase sales?' )
print(response)
