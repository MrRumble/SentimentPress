from flask import jsonify, request
from app import app
from lib.news_fetch_functions import *

@app.route("/query", methods=["POST"])
def query_route():
    data = request.get_json()
    query = data.get('query', '')
    news_results_df = fetch_and_process_query(query, 100)
    mean_sentiment = calculate_average_sentiment(news_results_df)
    positive_count = calculate_positive_sentiment_count(news_results_df)
    negative_count = negative_sentiment_count(news_results_df)

    # Get top and bottom three articles as dictionaries
    top3 = top_three_articles(news_results_df)
    bottom3 = bottom_three_articles(news_results_df)
    news_results = news_results_df.to_dict(orient='records')
    total_articles = len(news_results_df)

    query_info ={
        "total_articles": total_articles,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "mean_sentiment": mean_sentiment
    }


    response_data = {
        'query_info': query_info,
        'news_results': news_results,
        'top3': top3,
        'bottom3': bottom3
    }

    return jsonify(response_data)
