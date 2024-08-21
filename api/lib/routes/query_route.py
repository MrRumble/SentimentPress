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
    user_id = data.get('user_id')

    # Check if the query is already in the database for the day.
    result_if_cached = query_cache.get_query_result_if_exists_today(query_text)
    
    # Pull search_id and search_term from result_if_cached if exists.
    if result_if_cached:
        search_id = result_if_cached.get('_id')
        response_data_front_end = query_cache.format_cached_result(result_if_cached)
        
        search_metadata = processor.set_search_metadata(search_id, query_text, user_id)
        processor.save_search_metatdata_to_db(search_metadata)  
        
    else:
        response_data_front_end, search_result = processor.process_query(query_text, user_id)
        search_id = processor.save_search_result_to_db(search_result)

        search_metadata = processor.set_search_metadata(search_id, query_text, user_id)
        processor.save_search_metatdata_to_db(search_metadata)
 

    return jsonify(response_data_front_end)
