import os
import streamlit as st
from helper import get_chunks,get_conversation_chain,get_pdf,get_vectorstore,handle_user_question

def main():

    st.set_page_config(page_title="Chat with Multiple PDFs", page_icon="📚")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "processed_pdfs" not in st.session_state:
        st.session_state.processed_pdfs = False
    
    st.header("Chat with Multiple PDFs 📚")
    
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload PDF files and click 'Process'", 
            type=["pdf"],
            accept_multiple_files=True
        )
        
        if st.button("Process") and pdf_docs:
            with st.spinner("Processing PDFs..."):
                raw_text = get_pdf(pdf_docs)
                text_chunks = get_chunks(raw_text)
                st.write(f"Created {len(text_chunks)} text chunks")
                vectorstore = get_vectorstore(text_chunks)
                st.write("Created FAISS vectorstore for semantic search")
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.session_state.processed_pdfs = True
                
                st.success("Processing complete! You can now chat with your documents.")

    user_question = st.text_input("Ask a question about your PDFs:")
    if user_question and st.session_state.processed_pdfs:
        handle_user_question(user_question)
    
    if not st.session_state.processed_pdfs:
        st.info("Upload PDF documents and click 'Process' to get started")
        st.subheader("Example questions you can ask:")
        st.write("- What is the main topic of these documents?")
        st.write("- Summarize the key points in these PDFs.")
        st.write("- What are the conclusions from these documents?")
        st.write("- Compare the information between different documents.")

if __name__ == "__main__":
    main()