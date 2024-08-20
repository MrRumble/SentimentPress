from datetime import datetime
from api.lib.processors.sentiment_analyser import SentimentAnalyser
from api.lib.processors.news_processor import NewsProcessor
from api.lib.core.database_connection import DatabaseConnection
from api.lib.processors.article_summariser import ArticleSummariser


class QueryProcessor:
    def __init__(self):
        self.processor = NewsProcessor()
        self.analyser = SentimentAnalyser()
        self.database_connection = DatabaseConnection()
        self.summariser = ArticleSummariser()

    def process_query(self, query, user_id=None):
        # Fetch and process articles
        df_sorted = self.processor.fetch_and_process_query(query, 100)

        # Calculate sentiment metrics
        mean_sentiment = self.analyser.calculate_average_sentiment(df_sorted)
        positive_count = self.analyser.calculate_positive_sentiment_count(df_sorted)
        negative_count = self.analyser.calculate_negative_sentiment_count(df_sorted)
        ratio = self.analyser.calculate_sentiment_ratio(positive_count, negative_count)

        # Summarize top and bottom articles
        df_summarised = self.processor.summarise_top_bottom_articles(df_sorted)

        top3 = self.processor.top_three_articles(df_sorted)
        bottom3 = self.processor.bottom_three_articles(df_sorted)
        news_results = df_sorted.to_dict(orient='records')
        total_articles = len(df_sorted)

        # Prepare response data for front end
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

        # Prepare search result object
        current_datetime = datetime.now()
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
            "user_id": user_id  # Pull from local storage
        }

        return response_data_front_end, search_result_object

    def save_search_result_to_db(self, search_result):
        db_connection = self.database_connection.get_database()
        result = db_connection["search-results"].insert_one(search_result)
        return result.inserted_id

    def set_search_metadata(self, search_id:str, search_term:str, user_id:int):
        search_meta_data = {
            "search_date": datetime.now().strftime('%d-%m-%Y'),  # Convert datetime to string with the correct format
            "search_time": datetime.now().time().strftime('%H:%M:%S'),   # Get the current time
            "search_id": search_id,
            "search_term": search_term,
            "user_id": user_id
            }
        return search_meta_data
    
    def save_search_metatdata_to_db(self, search_metadata):
        db_connection = self.database_connection.get_database()
        db_connection["search-metadata"].insert_one(search_metadata)

    



