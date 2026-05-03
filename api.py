from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

# Path to the JSON file acting as our temporary database
DATA_FILE = "products.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/products")
async def get_products():
    """Returns the list of all monitor products."""
    return load_data()

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """Returns a specific product by its ID."""
    products = load_data()
    product = next((p for p in products if p.get("id") == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
