from flask import jsonify
from app import app
from lib.news_fetch_functions import *

#This is a test route to see if I can pass data across to Back-end server. 
@app.route("/test", methods=["GET"])
def test():
    df = fetch_and_process_query('southgate', 100)
    print("???????????????????????????????????SENTIMENT SCORE: ", calculate_average_sentiment(df))
    pos = calculate_positive_sentiment_count(df)
    neg = negative_sentiment_count(df)
    print("!! positive article count: ", pos)
    print("!! negative article count: ", neg)
    print("!! Ratio : ", calculate_sentiment_ratio(pos, neg))
    json_data = df.to_json(orient='records')
    return jsonify(json_data)
    
    #Health -> -0.39
    #charity -> -0.24
    #recover -> -0.17
    #death -> -0.24
    #gaza -> -0.57