from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="AI Agent-Based CRM System")

@app.get("/")
def root():
    return {"message": "Welcome to the AI Agent-Based CRM System API!"}
