import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi


class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        uri = os.getenv("MONGODB_URL")
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["sentiment-press"]


    def find_one_query(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def get_database(self):
        return self.db

    def close_connection(self):
        self.client.close()
