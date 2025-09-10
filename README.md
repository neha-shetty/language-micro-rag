# PolyglotRAG

A **Micro Retrieval-Augmented Generation (RAG) pipeline** for **language learning and translation**.  

This prototype demonstrates how RAG can power **multilingual Q&A, translation, and pronunciation support** by retrieving knowledge from a small curated dataset of FAQs in **French, German, and Italian**.  

Built as a **take-home assessment (2–4 hours)**, PolyglotRAG shows an end-to-end workflow: **data preparation → ingestion → retrieval → generation with citations**.  

---

## Assessment Requirements

- ✅ Tiny dataset: ≥10 short Markdown/FAQ files (≤1k tokens each)  
- ✅ `questions.json`: 3–5+ answerable queries  
- ✅ `ingest.py`: load, chunk, embed, and store vectors  
- ✅ `answer.py`: retrieve relevant chunks & call a local LLM  
- ✅ README with setup, run commands, chunking choices, and tech rationale  

---

##  What I Built

- ** Dataset** — `sample_data/` with 12 multilingual FAQ files (French, German, Italian)  
- ** Queries** — `questions.json` with 10 realistic language-learning questions  
- ** Ingestion** — `ingest.py` chunks files (500 chars, 50 overlap), embeds with Hugging Face `sentence-transformer`, and stores vectors in a local FAISS index  
- ** Retrieval + Generation** — `answer.py` retrieves top matches, queries a local Ollama LLM (Llama3), and returns **answers with translations, pronunciations, and citations**, saved to `answers.json`  

---

## 🛠 How to Run

```bash
# 1️⃣ Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Build FAISS index
python ingest.py

# 4️⃣ Run RAG-based Q&A
python answer.py

# 5️⃣ (Optional) Run quick test
python test_answer.py
