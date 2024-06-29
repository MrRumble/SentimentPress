from flask import jsonify, request
from app import app
from .process_query_functions import process_query, save_search_result_to_db

@app.route("/query", methods=["POST"])
def query_route():
    data = request.get_json()
    query = data.get('query', '')

    response_data_front_end, search_result = process_query(query)
    save_search_result_to_db(search_result)

    return jsonify(response_data_front_end)
