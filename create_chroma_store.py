import os
from langchain_community.vectorstores import Chroma

DB_DIR = "./chroma_db"
def create_vector_store(docs, embeddings):
    return Chroma.from_documents(documents=docs, embedding=embeddings, persist_directory=DB_DIR)
