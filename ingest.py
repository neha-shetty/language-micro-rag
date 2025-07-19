import os

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def main():
    data_folder = "/Users/nehashetty/memrise-micro-rag/sample_data"

    # Load all .md files
    loader = DirectoryLoader(
        data_folder,
        glob="**/*.md",
        loader_cls=TextLoader,
        show_progress=True
    )
    docs = loader.load()

    print(f"Loaded {len(docs)} files.")

    # Split docs into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    splits = splitter.split_documents(docs)

    print(f"Split into {len(splits)} chunks.")

    #using huggingface embeddings as its freee
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    #faiss vector store creation
    vectorstore = FAISS.from_documents(splits, embeddings)

    # Saving FAISS index locally
    vectorstore.save_local("faiss_index")

    print("Vector store saved to ./faiss_index")

if __name__ == "__main__":
    main()
