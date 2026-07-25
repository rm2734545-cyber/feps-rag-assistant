from langchain_community.vectorstores import Chroma
from 04_vector_representation import get_embedding_model

DB_DIR = "./chroma_db"
def get_retriever(k: int = 3):
    embeddings = get_embedding_model()
    vector_store = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    return vector_store.as_retriever(search_kwargs={"k": k})
