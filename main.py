# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "version": "1.0.0"}

@app.get("/products")
def search_products(channel_id: int = 1, catalog_id: int = 1):
    return {
        "value": [
            {"id": 1, "name": "Laptop", "price": 1299.99},
            {"id": 2, "name": "Phone", "price": 699.00}
        ]
    }
