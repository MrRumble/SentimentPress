from flask import Blueprint, jsonify, request
from .process_query import QueryProcessor
from flask_cors import CORS

from .token_manager import TokenManager

query_route = Blueprint('query_route', __name__)
CORS(query_route)
token_manager = TokenManager()
processor = QueryProcessor()


@query_route.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    query_text = data.get('query', '')
    payload = token_manager.verify_token(request.headers.get('Authorization'))
    user_id = payload.get('user_id', None) if payload else None

    response_data_front_end, search_result = processor.process_query(query_text, user_id)
    processor.save_search_result_to_db(search_result)

    return jsonify(response_data_front_end)
