📄 PDF Chatbot with Streamlit and OpenAI
This is an interactive chatbot built using Streamlit, LangChain, and OpenAI, designed to let users upload a PDF file and ask questions based on its content.

🔍 Features
📁 PDF Upload: Users can upload any PDF document directly through the web interface.

🧠 Intelligent Q&A: Asks questions and receives answers based on the uploaded content using OpenAI's GPT model.

✂️ Text Chunking: Uses LangChain's RecursiveCharacterTextSplitter to split large PDFs into manageable text chunks.

🔎 Semantic Search: Employs FAISS to perform vector-based similarity searches, retrieving the most relevant sections of the PDF.

💬 Chat Interface: Powered by OpenAI's gpt-3.5-turbo, delivering precise and contextual answers.

🧰 Technologies Used
Streamlit – Web application interface

PyPDF2 – PDF text extraction

LangChain – Text chunking, embeddings, and QA chain

OpenAI API – Language model for answering questions

FAISS – Vector storage for semantic similarity

🚀 How It Works
Upload a PDF document using the sidebar.

The text is extracted, chunked, and converted into embeddings.

When a question is asked, similar chunks are retrieved via FAISS.

The retrieved content is passed to OpenAI for generating a contextual answer.
