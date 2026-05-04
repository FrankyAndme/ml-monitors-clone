from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client["ml_monitors"]
products_collection = db["products"]

@app.get("/products")
async def get_products():
    """Returns the list of all monitor products from MongoDB."""
    products = []
    for product in products_collection.find():
        # Convert ObjectId to string for JSON serialization
        product["_id"] = str(product["_id"])
        # Map MongoDB _id to the expected 'id' field if necessary, 
        # though the frontend might need to be updated to use _id.
        # For compatibility with the previous JSON version, we add an 'id' field.
        product["id"] = product["_id"]
        products.append(product)
    return products

@app.get("/products/{product_id}")
async def get_product(product_id: str):
    """Returns a specific product by its MongoDB _id."""
    try:
        product = products_collection.find_one({"_id": ObjectId(product_id)})
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        product["_id"] = str(product["_id"])
        product["id"] = product["_id"]
        return product
    except Exception as e:
        # If product_id is not a valid ObjectId, it will raise an error
        raise HTTPException(status_code=400, detail=f"Invalid product ID format: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
