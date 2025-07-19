import json

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from ollama import Client  

def main():
    #loading the local embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    #load faiss index
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    #questions
    with open("questions.json", "r") as f:
        questions = json.load(f)

    #ollama connection
    client = Client(host="http://localhost:11434")

    results = []

    for q_obj in questions:
        q = q_obj["question"]  
        print(f"\n Question: {q}")

        #similarity search
        docs = vectorstore.similarity_search(q, k=3)

        sources = []
        context = ""
        for doc in docs:
            source_file = doc.metadata.get("source", "unknown")
            sources.append(source_file)
            context += doc.page_content + "\n"

        #prompt
        prompt = f"""You are a helpful language tutor. 
Use the context below to answer the question naturally.
If possible, provide the translation and a pronunciation guide.

Respond directly and naturally — do NOT say "According to the context".

---

Context:
{context}

Question:
{q}

Answer in a helpful, clear way:"""

        response = client.generate(model="llama3", prompt=prompt)
        final_answer = response['response']

        result = {
            "question": q,
            "answer": final_answer.strip(),
            "sources": list(set(sources))
        }

        results.append(result)

    #save answers in another file
    with open("answers.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\n All done! Answers saved to answers.json")

if __name__ == "__main__":
    main()
