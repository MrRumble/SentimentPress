import os
from datetime import datetime, timedelta
from newsapi import NewsApiClient
from dotenv import load_dotenv

"""
This class fetches article data from the newsAPI using the get_everything method of the newsAPI client.
Note that our access is limited, restricting the range of query parameters available.
With full access, numerous scalable features could be incorporated!"
"""


# TESTED

class NewsFetcher:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("NEWS_API_KEY")
        self.newsapi = NewsApiClient(api_key=api_key)
        self.yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

    def fetch_articles(self, query, page_size, language='en', from_date=None, to_date=None):
        if not from_date:
            from_date = self.yesterday_date
        if not to_date:
            to_date = self.yesterday_date
        articles = self.newsapi.get_everything(q=query, language=language, page_size=page_size, from_param=from_date,
                                               to=to_date)
        if articles['status'] == 'ok':
            return articles['articles']
        else:
            raise ValueError("Failed to fetch news articles. Check your api key or try again later.")
