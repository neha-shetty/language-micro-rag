# 📄 Take‑Home Assessment: Micro‑RAG Prototype

---

## 🎯 **Assessment Overview**

**Task:**  
The assessment required building a **Micro-RAG prototype** to demonstrate an end‑to‑end Retrieval‑Augmented Generation workflow within **2–4 hours**.  

**Requirements included:**
- ✅ Build a tiny dataset (≥10 short Markdown or plain‑text FAQ files, each ≤1k tokens).
- ✅ Add a `questions.json` file with 3–5+ answerable questions.
- ✅ Write `ingest.py`: load the files, chunk them, embed them, and store them in a vector store.
- ✅ Write `answer.py` or a notebook: load the index, retrieve relevant chunks, run an LLM call, and return answers with file-level citations.
- ✅ Include a short `README` explaining setup, run commands, chunking choices, and tech rationale.

---

## 📌 **What I built**

**✅ Tiny dataset**  
I created `sample_data/` with 12 Markdown FAQ files covering basic French, German, and Italian phrases. This simulates a real multilingual phrasebook. The folder includes `questions.json` with 10 realistic questions (e.g. “How do I say hello in German?”).

**✅ `ingest.py`**  
This script:
- Loads the FAQ files.
- Splits them into small, overlapping text chunks (~500 characters) to balance context with retrieval accuracy.
- Generates embeddings using a local Hugging Face `sentence-transformers` model (free to run).
- Stores all chunk embeddings in a local **FAISS** index for fast similarity search.

**✅ `answer.py`**  
This script:
- Loads the FAISS index.
- For each question in `questions.json`, runs a similarity search to find the most relevant chunks.
- Builds a context prompt.
- Sends the prompt to a **local LLM** running through **Ollama** (Llama3) to generate a natural answer.
- Outputs JSON with the answer and the source files used.

---

##  **Why these tech choices**

- **No paid APIs:** I used Hugging Face local embeddings + Ollama to run everything fully locally, with no OpenAI or cloud cost.
- **FAISS:** Simple, fast local vector store- perfect for local RAG prototyping.
- **Chunking:** Small overlapping chunks keep answers relevant but preserve context for short queries.
- **Ollama:** Runs a modern open‑source Llama3 model locally to generate answers, so the flow works offline.

---
