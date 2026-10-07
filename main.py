import os
from fastapi import FastAPI

app = FastAPI()

# Render automatically injects DATABASE_URL into environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "")

@app.get("/")
def read_root():
    return {"message": "FastAPI is running successfully!"}

@app.get("/db-check")
def check_db():
    if DATABASE_URL:
        return {"status": "Database URL is configured!"}
    return {"status": "No Database URL found"}