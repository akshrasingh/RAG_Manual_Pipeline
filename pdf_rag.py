import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import tempfile

st.set_page_config(page_title="RAG PDF Chat")

st.title("📄 Chat with your PDF")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Save temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    # Load PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    st.success("PDF loaded!")

    # Chunking
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = text_splitter.split_documents(documents)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Vector DB
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # LLM
    llm = Ollama(model="llama3")

    # Prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
Answer ONLY using the context below.
If not found, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    )

    # RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",  # IMPORTANT
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    # User input
    query = st.text_input("Ask a question:")

    if query:
        result = qa_chain({"query": query})

        st.subheader("Answer:")
        st.write(result["result"])

        with st.expander("📄 Sources"):
            for doc in result["source_documents"]:
                st.write(doc.page_content)