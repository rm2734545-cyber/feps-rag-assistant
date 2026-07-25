from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def generate_answer(query: str, context_docs: list, api_key: str):
    context_text = ""
    for doc in context_docs:
        page_num = doc.metadata.get("page", "غير معروف")
        context_text += f"\n(المصدر: صفحة {page_num})\n{doc.page_content}\n"
    
    system_prompt = "أنت مساعد أكاديمي. أجب بناءً على السياق مع ذكر رقم الصفحة:\n\nالسياق:\n{context}"
    prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{question}")])
    llm = ChatOpenAI(openai_api_key=api_key, openai_api_base="https://openrouter.ai/api/v1", model_name="openai/gpt-4o-mini")
    chain = prompt | llm
    return chain.invoke({"context": context_text, "question": query}).content
