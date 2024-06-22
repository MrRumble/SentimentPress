from flask import jsonify
from app import app
from lib.news_fetch_functions import *

#This is a test route to see if I can pass data across to Back-end server. 
@app.route("/test", methods=["GET"])
def test():
    df = fetch_and_process_query('Trump', 2)
    json_data = df.to_json(orient='records')
    return jsonify(json_data)
    