# 📄 PDF Chatbot with Streamlit, LangChain, and OpenAI

This project is an interactive, AI-powered chatbot application built with **Streamlit**, **LangChain**, and **OpenAI's GPT** models. It enables users to upload PDF documents and ask contextual questions, receiving intelligent and relevant answers extracted from the document content.

---

## 🔧 Project Overview

The goal of this application is to simplify the way users interact with large PDF documents by leveraging advanced **natural language processing** (NLP) and **semantic search**. This chatbot can be particularly useful for:

- Legal document reviews  
- Research papers  
- Technical manuals  
- Financial reports  
- Internal documentation  

---

## 💡 Key Features

- **PDF Upload**: Securely upload and parse any PDF document.
- **Text Extraction & Chunking**: Automatically extracts and segments content using LangChain’s `RecursiveCharacterTextSplitter`.
- **Vector Embeddings**: Generates semantic embeddings via OpenAI to capture contextual meaning.
- **Similarity Search**: Uses **FAISS** for fast, accurate retrieval of relevant text sections.
- **Conversational Q&A**: Integrates OpenAI’s GPT (e.g., `gpt-3.5-turbo`) to generate precise answers based on extracted data.
- **Intuitive UI**: Clean and interactive interface built with Streamlit.

---

## ⚙️ How It Works

1. **Upload** a PDF document through the sidebar interface.
2. The file is parsed, and the text is **extracted and chunked** into smaller segments.
3. **Embeddings** are generated for each chunk using OpenAI’s Embedding API.
4. When a user enters a question, FAISS performs a **semantic similarity search** to find the most relevant chunks.
5. These chunks, along with the user’s query, are passed to **OpenAI’s GPT model**, which generates a context-aware answer.




