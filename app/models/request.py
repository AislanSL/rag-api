from pydantic import BaseModel

class QARequest(BaseModel):
    pergunta: str
    