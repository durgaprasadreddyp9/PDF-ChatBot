import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI

OPENAI_API_KEY = 'sk-proj-dppgM4ivBMCDb3zSN1HBL4QW0z_MdESdhpLdyWIEwXaDsjtBbEg7smn7wCJyHF57gQVmBlqvEWT3BlbkFJiI4UF3PVLXCz5b4XoQHcA5ey7HSs_qraybl07j3ZiX49'

#upload PDF files
st.header('My First ChatBot')

with st.sidebar:
    st.title('Documents')
    file = st.file_uploader('Choose a file', type = 'pdf')

# Extract Text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        #st.write(text)


    # Break into Chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators = "\n",
        chunk_size= 1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    st.write(chunks)

    # Generating Embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)


    # Creating Vector Store
    vector_store = FAISS.from_texts(chunks, embeddings)

    # Get User question
    user_question = st.text_input("Start Typing")

    # Do Similarity Search
    if user_question:
        match = vector_store.similarity_search(user_question)
        st.write(match)

        #define the LLM
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature = 0,
            max_tokens = 1000,
            model_name = 'gpt-3.5-turbo'

        )

    # Output Results
    chain = load_qa_chain(llm,chain_type = 'stuff')
    response = chain.run(input_documents = match, question = user_question)
    st.write(response)





