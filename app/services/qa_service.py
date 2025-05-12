from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM

def build_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 100}
    )

    llm = OllamaLLM(model="llama3")

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )