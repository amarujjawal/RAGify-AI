# 🤖 RAGify AI

**RAGify AI** is a Generative AI-powered document assistant that enables users to chat with their PDF files using **Retrieval-Augmented Generation (RAG)**. Built with **Python, Streamlit, LangChain, LangGraph, and Google Gemini**, the application retrieves relevant information from uploaded documents and generates accurate, context-aware responses.

---

## 🚀 Features

* 📄 Upload one or multiple PDF documents
* 💬 Ask questions in natural language
* 🧠 Context-aware answers using RAG architecture
* 🔍 Semantic document retrieval with vector embeddings
* ✂️ Automatic text chunking for efficient indexing
* 🗂️ Conversational memory powered by LangGraph
* ⚡ Clean and interactive Streamlit interface
* 🔐 Environment variable support using `.env`

---

## 🏗️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **LLM:** Google Gemini
* **AI Framework:** LangChain
* **Workflow & Memory:** LangGraph
* **Embeddings:** Google Generative AI Embeddings
* **Vector Store:** InMemoryVectorStore
* **Document Loader:** PyPDFDirectoryLoader
* **Text Splitting:** RecursiveCharacterTextSplitter

---

## 📂 Project Structure

```text
RAGify-AI/
│── app.py
│── .env
│── requirements.txt
│── doc_files/
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/RAGify-AI.git
cd RAGify-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 🛠️ How It Works

1. Upload one or more PDF files.
2. The application extracts and splits the document text into chunks.
3. Google Generative AI Embeddings convert the chunks into vector representations.
4. Relevant chunks are retrieved through semantic similarity search.
5. The retrieved context is passed to the Gemini model.
6. Gemini generates an accurate answer grounded in the uploaded documents.

---

## 🎯 Use Cases

* Research paper exploration
* Academic study assistance
* Company policy and documentation search
* Technical manual Q&A
* Knowledge base chatbot
* Personal document assistant

---

## 🔮 Future Improvements

* Support for FAISS or ChromaDB persistence
* Source citations with page numbers
* DOCX and TXT document support
* Chat history export
* User authentication
* Cloud deployment and scalable storage

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to fork the repository, create a new branch, and submit a pull request.

---

## 📜 License

This project is available under the MIT License. You are free to use, modify, and distribute it in accordance with the license terms.

---

⭐ If you found this project useful, consider giving it a star on GitHub!

Deployment update


## 🚀 Live Demo

https://ragify-ai-oax8.onrender.com
