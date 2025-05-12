import os 
from typing import List 
from app.core.config import PDF_FOLDER
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents() -> List:
    documents = []
    for filename in os.listdir(PDF_FOLDER):
        if filename.endswith(".pdf"):
            path = os.path.join(PDF_FOLDER, filename)
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
    return documents

def split_documents(documents: List) -> List:
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)