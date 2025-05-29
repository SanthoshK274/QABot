import PyPDF2
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

def loaddoc(file):
    reader=PyPDF2.PdfReader(file)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text

def createvectorstore(doctext):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="Your_API_Key")
    splitter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    texts=splitter.split_text(doctext)
    vectorstore=FAISS.from_texts(texts,embeddings)
    return vectorstore

def response(query,doctext):
    vectorstore=createvectorstore(doctext)
    qabot=RetrievalQA.from_chain_type(
        llm=ChatGoogleGenerativeAI(google_api_key="Your_API_Key",
                                   model="gemini-2.0-flash",
                                   temperature=0,
                                   max_tokens=None,
                                   timeout=None,
                                   max_retries=2),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    result = qabot.run(query)
    return result
