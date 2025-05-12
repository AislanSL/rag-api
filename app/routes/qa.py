from fastapi import APIRouter
from app.models.request import QARequest
from app.services.loader_service import load_documents, split_documents
from app.services.embedding_service import get_embeddings
from app.services.vector_service import create_collection, store_vectors
from app.services.qa_service import build_qa_chain

router = APIRouter()

@router.post("/qa")
def question_answer(req: QARequest):
    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = get_embeddings()

    create_collection(embeddings)
    vectorstore = store_vectors(chunks, embeddings)
    qa_chain = build_qa_chain(vectorstore)

    response = qa_chain.invoke({"query": req.pergunta})

    return {
        "resposta": response["result"],
        "documentos": [
            {"fonte": doc.metadata["source"], "conteudo": doc.page_content[:200]}
            for doc in response["source_documents"]
        ]
    }
