from flask import Blueprint, jsonify, request
from .process_query import QueryProcessor
from flask_cors import CORS

query_route = Blueprint('query_route', __name__)
CORS(query_route)


@query_route.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    query_text = data.get('query', '')

    processor = QueryProcessor()
    response_data_front_end, search_result = processor.process_query(query_text)
    processor.save_search_result_to_db(search_result)

    return jsonify(response_data_front_end)
