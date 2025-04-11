import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")
mongo_collection = os.getenv("MONGO_COLLECTION")

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

def get_profile_by_slug(slug):
    return collection.find_one({"slug": slug})

# profiles_loader.py
def get_profile_by_name(name: str):
    # Split name into first and last parts
    name_parts = name.lower().strip().split()
    if len(name_parts) < 2:
        return None

    first, last = name_parts[0], name_parts[1]

    return collection.find_one({
        "firstName": {"$regex": f"^{first}$", "$options": "i"},
        "lastName": {"$regex": f"^{last}$", "$options": "i"},
    })
