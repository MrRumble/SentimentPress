# utils.py
from datetime import datetime
from lib.news_fetch_functions import *
from lib.database_connection import get_db


def process_query(query):
    # Pipeline calls, two slow functions.
    news_results_df = fetch_and_process_query(query, 100)
    df_summarised = summarise_top_bottom_articles(news_results_df)

    mean_sentiment = calculate_average_sentiment(news_results_df)
    positive_count = calculate_positive_sentiment_count(news_results_df)
    negative_count = negative_sentiment_count(news_results_df)
    ratio = calculate_sentiment_ratio(positive_count, negative_count)
    current_datetime = datetime.now()

    # Get top and bottom three articles as dictionaries
    top3 = top_three_articles(news_results_df)
    bottom3 = bottom_three_articles(news_results_df)
    news_results = news_results_df.to_dict(orient='records')  # Every article
    total_articles = len(news_results_df)

    query_info_front_end = {
        "total_articles": total_articles,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "mean_sentiment": mean_sentiment,
        'summary': df_summarised
    }

    response_data_front_end = {
        'query_info': query_info_front_end,
        'news_results': news_results,
        'top3': top3,
        'bottom3': bottom3
    }

    search_result_object = {
        "search_term": query,
        "search_date": current_datetime,
        "sentiment_score": mean_sentiment,
        "positive_article_count": positive_count,
        "negative_article_count": negative_count,
        "total_article_count": total_articles,
        "ratio_positive_vs_negative": ratio,
        "main_headline": df_summarised,
        "top_3_articles": top3,
        "bottom_3_articles": bottom3,
        "user_id": None  # Pull from local storage
    }

    return response_data_front_end, search_result_object


def save_search_result_to_db(search_result):
    db_connection = get_db()
    db_connection["search-results"].insert_one(search_result)
