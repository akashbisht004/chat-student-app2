# Chat with Multiple PDFs 📚

This Streamlit app allows you to upload multiple PDF documents, process them, and then interact with the content through a conversational interface. You can ask questions based on the content of the PDFs, and the app will provide relevant answers based on semantic search using a vectorstore.

## Features

- Upload multiple PDF documents.
- Process the PDFs to extract and chunk the text.
- Perform semantic search using FAISS vectorstore for relevant answers.
- Ask questions related to the content of the PDFs.

## Requirements

Before running this app, ensure you have the following Python libraries installed:

- `streamlit`
- `PyPDF2` (or another PDF parsing library)
- `faiss-cpu` (for vector storage and semantic search)
- `openai` (or another language model API for conversation chain)

You can install these dependencies using `pip`:

```bash
pip install streamlit PyPDF2 faiss-cpu openai
