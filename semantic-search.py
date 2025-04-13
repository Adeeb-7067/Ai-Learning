import os
from typing import List
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load .env if needed
load_dotenv()

# Step 1: Load file (TXT or PDF)
def load_file(file_path: str):
    if file_path.lower().endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.lower().endswith(".txt"):
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file format. Use .txt or .pdf.")
    return loader.load()

file_path = "sample.txt"  # Change to your file
documents = load_file(file_path)
print(f"\n✅ Loaded {len(documents)} document(s).\n")

# Step 2: Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = text_splitter.split_documents(documents)
print(f"🧩 Split into {len(chunks)} chunks.\n")

# Step 3: Load embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 4: Create FAISS vector store
vectorstore = FAISS.from_documents(chunks, embedding_model)

# Step 5: Accept user query and search
query = input("🔍 Enter your query: ")
results = vectorstore.similarity_search_with_score(query, k=3)

# Step 6: Show results
print("\n📄 Top Relevant Chunks:")
for i, (doc, score) in enumerate(results):
    print(f"\nResult #{i+1}")
    print(f"Score: {score:.4f}")
    print(f"Content:\n{doc.page_content}")
