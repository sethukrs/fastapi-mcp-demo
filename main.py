# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def search_products(channel_id: int = 1, catalog_id: int = 1):
    return {
        "value": [
            {"id": 1, "name": "Laptop", "price": 1299.99},
            {"id": 2, "name": "Phone", "price": 699.00}
        ]
    }

@app.get("/carts")
def get_carts(user_id: int = 1):
    return {
        "carts": [
            {"cart_id": 1, "user_id": user_id, "items": [
                {"product_id": 1, "quantity": 2},
                {"product_id": 2, "quantity": 1}
            ]}
        ]
    }
