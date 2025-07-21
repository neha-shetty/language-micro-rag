# 📄 Take‑Home Assessment: Micro‑RAG Prototype

---

# 📚 Micro‑RAG Assessment

**Task:**  
The assessment required building a **Micro-RAG prototype** to demonstrate an end‑to‑end Retrieval‑Augmented Generation workflow within **2–4 hours**.  

**Requirements included:**
- ✅ Build a tiny dataset (≥10 short Markdown or plain‑text FAQ files, each ≤1k tokens).
- ✅ Add a `questions.json` file with 3–5+ answerable questions.
- ✅ Write `ingest.py`: load the files, chunk them, embed them, and store them in a vector store.
- ✅ Write `answer.py` or a notebook: load the index, retrieve relevant chunks, run an LLM call, and return answers with file-level citations.
- ✅ Include a short `README` explaining setup, run commands, chunking choices, and tech rationale.


---

## ✅ What I did

- **Tiny dataset:**  
  Created `sample_data/` with 12 short Markdown FAQ files (French, German, Italian). Each file is under 1k tokens, clean, simple, and legal.

- **Prepared realistic queries:**  
  `questions.json` has 10 practical language questions.

- **Ingestion pipeline:**  
  `ingest.py` loads the folder, splits files into 500-character chunks with 50 overlap (to keep sentence meaning), embeds them using a free Hugging Face `sentence-transformer`, and stores dense vectors in a local FAISS index.

- **Dense retrieval & generation:**  
  `answer.py` loads the index, runs a similarity search for each question, then calls a local Ollama LLM (Llama3) to generate natural answers, including translations and pronunciation. Results are printed clearly and saved to `answers.json` with file-level citations.

- **Virtual environment:**  
  Used a Python virtual environment (`venv/`) to isolate dependencies and keep the setup reproducible and conflict-free.

---

## How to run

# Create & activate venv
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Build the FAISS index
python ingest.py

# Run the local LLM answers
python answer.py

# (Optional) Run a quick test
python test_answer.py

