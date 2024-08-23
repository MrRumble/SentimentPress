from pymongo import MongoClient
from api.lib.core.database_connection import DatabaseConnection

db = DatabaseConnection().get_database()

collection = db["search-metadata"]
# Iterate over each document and update the search_term field to lowercase
for document in collection.find({}):
    if 'search_term' in document:
        updated_search_term = document['search_term'].lower()
        collection.update_one(
            {'_id': document['_id']},
            {'$set': {'search_term': updated_search_term}}
        )

print("All search_term fields have been updated to lowercase.")

