from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"status": "FastAPI is running!"}

@app.post("/test-post")
def create_item(item: Item):
    return {
        "message": "POST request received successfully!",
        "item_received": item
    }