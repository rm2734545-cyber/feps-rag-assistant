import streamlit as st
import importlib

retrieve_module = importlib.import_module("retrieve_context")
prompt_module = importlib.import_module("prompting")

st.title("🎓 المساعد الأكاديمي للائحة الكلية")
api_key = st.secrets.get("OPENROUTER_API_KEY", "")

query = st.text_input("أدخل سؤالك هنا:")
if st.button("بحث") and query and api_key:
    docs = retrieve_module.get_retriever().invoke(query)
    ans = prompt_module.generate_answer(query, docs, api_key)
    st.write(ans)
