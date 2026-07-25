from typing import List
from langchain_core.documents import Document
def clean_documents(documents: List[Document]) -> List[Document]:
    for doc in documents:
        doc.page_content = "\n".join([line.strip() for line in doc.page_content.splitlines() if line.strip()])
    return documents
