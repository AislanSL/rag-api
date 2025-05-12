from fastapi import FastAPI
from app.routes import qa, health

app = FastAPI()

app.include_router(qa.router, prefix="/api")
app.include_router(health.router)
