import json
import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def migrate():
    # Get MongoDB URI from environment variable or use default local
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    db_name = os.getenv("MONGO_DB", "ml_monitors")
    
    print(f"Connecting to MongoDB at {mongo_uri}...")
    try:
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        # Trigger a connection check
        client.admin.command('ping')
        print("Connected successfully!")
    except ConnectionFailure:
        print("Could not connect to MongoDB. Please check your MONGO_URI.")
        return

    db = client[db_name]
    collection = db["products"]

    # Load products from JSON
    try:
        with open("products.json", "r", encoding="utf-8") as f:
            products = json.load(f)
    except FileNotFoundError:
        print("products.json not found. Migration aborted.")
        return
    except json.JSONDecodeError:
        print("Error decoding products.json.")
        return

    # Clear existing data to avoid duplicates during testing
    collection.delete_many({})

    # Insert data
    if isinstance(products, list):
        result = collection.insert_many(products)
        print(f"Successfully migrated {len(result.inserted_ids)} products to MongoDB.")
    else:
        print("Expected products.json to contain a list of products.")

    client.close()

if __name__ == "__main__":
    migrate()
