from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

def get_db():
    # Replace the placeholder with your Atlas connection string
    load_dotenv()
    uri = os.getenv("MONGODB_URL")
    # Set the Stable API version when creating a new client
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["sentiment-press"]
    return db