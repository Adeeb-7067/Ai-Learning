# semantic-search.py

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Step 1: Load your file
loader = TextLoader("sample.txt")
documents = loader.load()

# Step 2: Chunk it
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = text_splitter.split_documents(documents)

# Step 3: Load Embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 4: Create vector store
vectorstore = FAISS.from_documents(chunks, embedding_model)

# Step 5: Search
query = "What is this document about?"
results = vectorstore.similarity_search_with_score(query, k=3)

# Step 6: Show results
print("\nTop Relevant Chunks:")
for i, (doc, score) in enumerate(results):
    print(f"\nResult #{i+1}")
    print(f"Score: {score}")
    print(f"Content:\n{doc.page_content}")
