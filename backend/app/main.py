from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.api.api_v1 import api_router

load_dotenv()

app = FastAPI(title="AI Agent-Based CRM System")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the AI Agent-Based CRM System API!"}
