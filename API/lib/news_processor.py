from .news_fetcher import NewsFetcher
from .article_processor import ArticleProcessor
from .sentiment_analyser import SentimentAnalyser
from .article_summariser import ArticleSummariser
from .data_handler import DataHandler

"""
This class serves as the core component of our system, encapsulating all functionalities related to news and articles.
It handles the extraction of articles from a search query and identifies the top and bottom three articles based on sentiment scores. 
The 'query' parameter, received from the front-end server via query_route.py, is processed through the 'fetch_and_process_query' method."
"""
#TESTED 

class NewsProcessor:
    def __init__(self):
        self.fetcher = NewsFetcher()
        self.processor = ArticleProcessor()
        self.summarizer = ArticleSummariser() # <- 
        self.analyzer = SentimentAnalyser()
        self.data_handler = DataHandler()

    def fetch_and_process_query(self, query, page_size):
        articles = self.fetcher.fetch_articles(query, page_size)
        processed_articles = [self.processor.process_article(article) for article in articles if self.processor.process_article(article) is not None]
        df = self.data_handler.create_dataframe(processed_articles)
        df_sorted = self.data_handler.sort_dataframe(df)
        return df_sorted

    def top_three_articles(self, df):
        top_articles_df = df.nlargest(3, 'Sentiment Score')
        articles = [
            {
                "title": row['Title'],
                "description": row['Description'],
                "published_date": row['Published Date'],
                "source": row['Source'],
                "sentiment": row['Sentiment Score']
            }
            for _, row in top_articles_df.iterrows()
        ]
        return articles

    def bottom_three_articles(self, df):
        bottom_articles_df = df.nsmallest(3, 'Sentiment Score')
        articles = [
            {
                "title": row['Title'],
                "description": row['Description'],
                "published_date": row['Published Date'],
                "source": row['Source'],
                "sentiment": row['Sentiment Score']
            }
            for _, row in bottom_articles_df.iterrows()
        ]
        return articles

#CHECK IF THIS IS NEEDED
    def summarise_top_bottom_articles(self, df, top_n=3, bottom_n=3, max_summary_sentences=6):
        return self.summarizer.summarise_top_bottom_articles(df, top_n, bottom_n, max_summary_sentences) 
