import streamlit as st
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer, CrossEncoder
from transformers import pipeline

# Load the FAISS index, embeddings, and chunks from the .pkl file
@st.cache_resource
def load_index():
    with open("pdf_index.pkl", "rb") as f:
        index, embeddings, chunks = pickle.load(f)
    return index, embeddings, chunks

# Query Retrieval
def retrieve(query, index, chunks, model, reranker, k=5):
    query_emb = model.encode([query])
    _, I = index.search(query_emb, k)

    # Retrieve relevant chunks
    retrieved = [chunks[i] for i in I[0]]

    # Rerank with Cross-Encoder
    pairs = [[query, passage] for passage in retrieved]
    scores = reranker.predict(pairs)

    # Sort by score
    ranked_results = sorted(zip(retrieved, scores), key=lambda x: x[1], reverse=True)

    # Return top-ranked chunks
    return [r[0] for r in ranked_results]

# Question-Answering Generation
def generate_answer(query, retrieved_text):
    qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")

    best_answer = None
    best_score = 0

    for context in retrieved_text:
        result = qa_model(question=query, context=context)

        if result['score'] > best_score:
            best_score = result['score']
            best_answer = result['answer']

    return best_answer if best_answer else "No relevant answer found."

# Streamlit App
st.title("📚 PDF Querying")
st.write("Upload a PDF and query it using RAG")

# Load the model and reranker
model = SentenceTransformer('all-MiniLM-L6-v2')
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# File uploader
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    # Save PDF to disk for processing
    pdf_path = "uploaded_pdf.pdf"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    # Run the indexing script
    st.info("Indexing the PDF... This may take a few seconds.")
    import os
    os.system(f"python index_pdf.py {pdf_path}")

    # Load the saved index
    index, embeddings, chunks = load_index()

    # Query section
    query = st.text_input("Enter your query:")
    if st.button("Search"):
        if query:
            retrieved_text = retrieve(query, index, chunks, model, reranker)
            answer = generate_answer(query, retrieved_text)
            st.write("### 🔥 Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a query.")
