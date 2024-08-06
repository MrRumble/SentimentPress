from flask import Blueprint, jsonify, request
from api.lib.processors.process_query import QueryProcessor
from flask_cors import CORS
from api.lib.core.query_cache_manager import QueryCacheManager
from api.lib.core.token_manager import TokenManager

query_route = Blueprint('query_route', __name__)
CORS(query_route)
token_manager = TokenManager()
processor = QueryProcessor()
query_cache = QueryCacheManager()


@query_route.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    query_text = data.get('query', '')
    payload = token_manager.verify_token(request.headers.get('Authorization'))
    user_id = payload.get('user_id', None) if payload else None

    # Check if the query is already in the database for the day.
    result_if_cached = query_cache.get_query_result_if_exists_today(query_text)
    if result_if_cached:
        print("Result already in database")
        print(response_data_front_end)
        response_data_front_end = query_cache.format_cached_result(result_if_cached)
        # TODO save the duplicate query to the db, 
        # might be useful to get count data of a query.

    else:
        response_data_front_end, search_result = processor.process_query(query_text, user_id)
        processor.save_search_result_to_db(search_result)

    return jsonify(response_data_front_end)
