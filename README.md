# 📄 Multi-Document Reader with RAG & LLM

This repository contains a powerful **Multi-Document Reader** that utilizes **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLMs)** to process and extract insights from multiple documents. The project is built using **Python** and a user-friendly interface powered by **Streamlit**.

## 🚀 Features
- 📑 **Multi-Document Support** – Upload multiple documents (PDF, TXT, DOCX, etc.) for processing.
- 🔍 **RAG-based Query Processing** – Combines retrieval and generation to provide accurate and context-aware responses.
- 🤖 **LLM-Powered Summarization & Q&A** – Extracts key information and answers queries intelligently.
- ⚡ **Fast & Scalable** – Optimized for speed and efficient document handling.
- 🎨 **Interactive UI with Streamlit** – Simple, elegant, and easy to use.
- 💸 **Uses Together API for Free LLM Access** – Leverages Mistral AI and other open models via Together AI.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **LLM:** Together AI (mistralai/Mistral-7B-Instruct-v0.2)
- **Vector Database:** FAISS
- **Document Processing:** LangChain, PdfReader
- **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
- **Memory:** Conversation Buffer Memory for chat history

## 📥 Installation
```bash
git clone https://github.com/akashbisht004/chat-student-app2.git
cd multi-document-reader-rag
pip install -r requirements.txt
```

## 🔑 Setup Together API
1. Get your free API key from [Together AI](https://www.together.xyz/).
2. Create a `.env` file and add your API key:
   ```env
   TOGETHER_API_KEY=your_api_key_here
   ```

## 📄 How It Works
1. **PDF Processing:**
   - Uploaded PDFs are read using `PdfReader`.
   - Extracted text is split into chunks of 1000 characters with 200-character overlap using `RecursiveCharacterTextSplitter`.

2. **Vector Storage:**
   - `HuggingFaceEmbeddings` (all-MiniLM-L6-v2) converts text chunks into embeddings.
   - `FAISS` stores and retrieves relevant chunks based on user queries.

3. **Conversational AI:**
   - `Together` API is used with the `Mistral-7B-Instruct-v0.2` model for generating responses.
   - `ConversationBufferMemory` maintains chat history.
   - `ConversationalRetrievalChain` integrates the LLM with the vector retriever for improved responses.

4. **User Interaction:**
   - Users enter queries in Streamlit UI.
   - The model retrieves relevant context and generates intelligent responses.
   - Chat history is displayed interactively.

## 🚀 Usage
```bash
streamlit run app.py
```
Upload your documents and start querying them with AI-powered retrieval!

## 🤝 Contributing
Feel free to fork this repository, create a new branch, and submit a pull request with improvements!

⭐ **Star** this repository if you find it useful!

