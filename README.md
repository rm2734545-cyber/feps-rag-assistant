# 🎓 المساعد الأكاديمي للائحة الكلية (FEPS RAG Assistant)

نظام ذكي متكامل للإجابة على استفسارات الطلاب والباحثين المتعلقة باللائحة الأكاديمية لكلية الاقتصاد والعلوم السياسية، باستخدام تقنية **RAG (Retrieval-Augmented Generation)**.

---

## 🌟 الميزات الرئيسية (Key Features)
* **إجابات دقيقة موثوقة:** يعتمد النظام كلياً على نص اللائحة الرسمية دون التسبب في أخطاء أو معلومات خاطئة (No Hallucinations).
* **بحث دلالي ذكي (Semantic Search):** يفهم استعلامات المستخدم باللغة العربية والعامية ويطابقها مع النصوص ذات الصلة.
* **واجهة سهلة وسريعة:** تم بناء الواجهة باستخدام Streamlit لتوفير تجربة استخدام بسيطة وسريعة.

---

## 🏗️ البنية التقنية (System Architecture & Pipeline)

يعمل المشروع وفق نموذج RAG مقسم إلى عدة وحدات برمجية متتالية:

1. **`documents.py` & `preprocessing.py`**: قراءة ملفات اللائحة وتنظيف النصوص واستخراجها.
2. **`chunking.py`**: تقسيم النص الكامل إلى أجزاء صغرى (Chunks) لسهولة البحث.
3. **`vector_representation.py`**: تحويل النصوص إلى متجه عددي (Embeddings).
4. **`create_chroma_store.py`**: حفظ المتجهات في قاعدة بيانات متجهة (**ChromaDB**).
5. **`retrieve_context.py`**: استرجاع الفقرات الأكثر صلة بطلب المستخدم عند استلام السؤال.
6. **`prompting.py`**: بناء الـ Prompt وتمريره لنموذج الذكاء الاصطناعي عبر **OpenRouter API**.
7. **`streamlit_app.py`**: واجهة المستخدم التفاعلية العارضة للنتائج.

---

## 🛠️ التقنيات المستخدمة (Tech Stack)
* **Language:** Python 3.11
* **Framework:** Streamlit
* **Vector Database:** ChromaDB
* **LLM Integration:** OpenRouter API
* **Version Control & Hosting:** GitHub / Streamlit Cloud
