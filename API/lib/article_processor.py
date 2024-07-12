from transformers import pipeline

"""
This class processes individual articles, 
extracting specified information and analyzing sentiment scores using a Transformer pipeline 
on combined titles and descriptions. 
Note: sentiment analysis is slow; consider a faster model based on our needs. 
With full access to a newsAPI key, particularly access to article content, sentiment scoring accuracy could improve. 
Articles are validated to prevent null results from deleted publications. 
Finally, articles are transformed into a delicious dictionary format, ready for use elsewhere.
"""


# TESTED
class ArticleProcessor:
    def __init__(self):
        self.sentiment_pipeline = pipeline('sentiment-analysis')

    def extract_article_info(self, article):
        title = article['title']
        description = article['description']
        published_at = article['publishedAt']
        source = article['source'].get('name')
        return title, description, published_at, source

    def combine_text(self, title, description):
        return f"{title}. {description}"

    def analyse_sentiment(self, text):
        if text:
            sentiment = self.sentiment_pipeline(text)
            sentiment_score = sentiment[0]['score'] if sentiment[0]['label'] == 'POSITIVE' else -sentiment[0]['score']
        else:
            sentiment_score = None
        return sentiment_score

    def validate_article(self, title, description, sentiment_score):
        if sentiment_score != 0 and title is not None and description is not None:
            return '[Removed]' not in title and '[Removed]' not in description
        return False

    def process_article(self, article):
        title, description, published_at, source = self.extract_article_info(article)
        text = self.combine_text(title, description)
        sentiment_score = self.analyse_sentiment(text)
        if self.validate_article(title, description, sentiment_score):
            return {
                'Published Date': published_at,
                'Title': title,
                'Description': description,
                'Source': source,
                'Sentiment Score': sentiment_score
            }
        return None
