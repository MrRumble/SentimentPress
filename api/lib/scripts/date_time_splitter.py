from pymongo import MongoClient
from api.lib.core.database_connection import DatabaseConnection
from bson import ObjectId
from datetime import datetime

db = DatabaseConnection().get_database()

collection = db["search-results"]
# Iterate over each document and update the search_term field to lowercase
for document in collection.find({}):
    if 'search_date' in document and isinstance(document['search_date'], datetime):
        search_date_time = document['search_date']
        print(search_date_time)

        updated_time = search_date_time.strftime('%H:%M:%S')
        print(updated_time)
        updated_date = search_date_time.strftime('%d-%m-%Y')
        print(updated_date)

        collection.update_one(
                {'_id': document['_id']},
                {'$set': {'search_date': updated_date, 'search_time': updated_time}}
            )


