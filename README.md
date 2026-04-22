# 📄 PDF RAG Chat App

An AI-powered application that allows users to upload a PDF and ask questions about its content using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* 📄 Upload any PDF document
* 💬 Ask questions in natural language
* 🧠 Answers generated using your document (not generic AI)
* 🔍 Uses semantic search (FAISS) for accurate retrieval
* 🧾 Displays source chunks for transparency

---

## 🧠 Tech Stack

* **Frontend/UI:** Streamlit
* **Backend:** Python
* **RAG Framework:** LangChain
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **Vector Database:** FAISS
* **LLM:** Llama3 via Ollama

---

## ⚙️ How It Works

```text
PDF → Text → Chunking → Embeddings → FAISS → Retrieval → Prompt → LLM → Answer
```

---

## 📦 Installation & Setup

### 🔹 1. Clone the repository

```bash
git clone https://github.com/akshrasingh/RAG_Manual_Pipeline.git

```

---



### 🔹 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 4. Install Ollama (for local LLM)

Download and install Ollama from:

https://ollama.com

Then pull the model:

```bash
ollama run llama3
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📌 Usage

1. Upload a PDF
2. Wait for processing
3. Ask questions like:

   * "What is Kubernetes?"
   * "Summarize this document"
4. View answers + source context

---

## ⚠️ Notes

* Ensure Ollama is running locally
* First run may take time (embedding + indexing)
* CPU-based FAISS is used (no GPU required)

---

## 🧠 Learning Outcomes

* Built a complete RAG pipeline from scratch
* Integrated embeddings, vector search, and LLM
* Created a functional AI application with UI

---

## 🚀 Future Improvements

* Chat history (memory)
* Better UI (chat-style interface)
* Deployment (Streamlit Cloud / AWS)
* Multi-document support

---

## 📬 Author

Akshra Singh
