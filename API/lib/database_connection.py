from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

def get_db():
    load_dotenv()
    uri = os.getenv("MONGODB_URL")
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["sentiment-press"]
    return db