from api.lib.core.database_connection import DatabaseConnection
import datetime

class QueryCacheManager:
    """
    The QueryCacheManager class is responsible for managing and 
    handling cached query results within the application. 
    Its primary functions are to check for the existence of cached query 
    results for the current day and format these results to match the 
    required response structure for the API.
    """
    def __init__(self) -> None:
        self.db = DatabaseConnection()
        self.date_today = datetime.datetime.now().strftime("%Y-%m-%d")

    def get_query_result_if_exists_today(self, query: str) -> dict:
        search_query = {
            "$expr": {
                "$and": [
                    {"$eq": [{"$dateToString": {"format": "%Y-%m-%d", "date": "$search_date"}}, self.date_today]},
                    {"$eq": ["$search_term", query]}
                ]
            }
        }
        
        result = self.db.find_one_query("search-results", search_query)
        print('RESULT TYPE IF CACHED!!!!!!', type(result))
        return result

    def format_cached_result(self, result):
        # Convert the cached result to the desired response format
        return {
            'query_info': {
                "total_articles": result.get("total_article_count", 0),
                "positive_count": result.get("positive_article_count", 0),
                "negative_count": result.get("negative_article_count", 0),
                "mean_sentiment": result.get("sentiment_score", 0),
                'summary': result.get("main_headline", "")
            },
            'news_results': result.get("news_results", []),
            'top3': result.get("top_3_articles", []),
            'bottom3': result.get("bottom_3_articles", [])
        }