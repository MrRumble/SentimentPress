import pandas as pd
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from transformers import pipeline
import os
from dotenv import load_dotenv
import matplotlib

from models.article import Article #transformers library uses advanced machine learning and trained on large text models

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=api_key)

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Calculate the date for yesterday
yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

def fetch_articles(query, page_size, language='en', from_date=yesterday_date, to_date=yesterday_date):
    articles = newsapi.get_everything(q=query, language=language, page_size=page_size, from_param=from_date, to=to_date)
    if articles['status'] == 'ok':
        return articles['articles']
    else:
        raise ValueError("Failed to fetch news articles. Check your API key or try again later.")

def extract_article_info(article):
    title = article['title']
    description = article['description']
    published_at = article['publishedAt'] #type str
    source = article['source'].get('name')
    return title, description, published_at, source

def combine_text(title, description):
    return f"{title}. {description}"

def analyse_sentiment(text):
    if text:
        sentiment = sentiment_pipeline(text)
        sentiment_score = sentiment[0]['score'] if sentiment[0]['label'] == 'POSITIVE' else -sentiment[0]['score']
    else:
        sentiment_score = None
    return sentiment_score

#Some articles are removed from news source after publishing, still recorded on API 
# so need to be cleaned out.
def validate_article(title, description, sentiment_score):
    if sentiment_score != 0 and title is not None and description is not None:
        if '[Removed]' not in title and '[Removed]' not in description:
            return True
    return False


def process_article(article):
    title, description, published_at, source = extract_article_info(article)
    text = combine_text(title, description)
    sentiment_score = analyse_sentiment(text)
    if validate_article(title, description, sentiment_score):
        return {
            'Published Date': published_at,
            'Title': title,
            'Description': description, 
            'Source': source,
            'Sentiment Score': sentiment_score
        }
    return None

def create_dataframe(article_data): #I GOT HERE!
    return pd.DataFrame(article_data)  

def sort_dataframe(df, column='Sentiment Score'):
    return df.sort_values(by=column, ascending=False)

def fetch_and_process_query(query, page_size): #Combines all of the above functions (the holy grail)
    articles = fetch_articles(query, page_size)
    processed_articles = [process_article(article) for article in articles if process_article(article) is not None]
    df = create_dataframe(processed_articles)
    df_sorted = sort_dataframe(df)
    return df_sorted

def top_three_articles(df):
    articles = []
    sorted_df = df.sort_values(by='Sentiment Score', ascending=False)
    for idx, row in sorted_df.head(3).iterrows():
        title = row['Title']
        description = row['Description']
        published_date = row['Published Date']
        source = row['Source']
        sentiment = row['Sentiment Score']
        article = Article(None, title, description, published_date, source, sentiment)
        articles.append(article)
    return articles

def bottom_three_articles(df):
    articles = []
    sorted_df = df.sort_values(by='Sentiment Score')
    for idx, row in sorted_df.head(3).iterrows():
        title = row['Title']
        description = row['Description']
        published_date = row['Published Date']
        source = row['Source']
        sentiment = row['Sentiment Score']
        article = Article(None, title, description, published_date, source, sentiment)
        articles.append(article)
    return articles

#TODO Handle cases where no articles are returned from query
#TODO Handle cases where articles returned are less than 6



#######################################
# Additional functions below, not yet used in app, so havent been tested yet
#######################################

# def create_box_plot(df):
#     return df.boxplot(column=df['Sentiment Score'])

def calculate_average_sentiment(df): 
    return df['Sentiment Score'].mean()

def calculate_positive_sentiment_count(df):
    return len(df[df['Sentiment Score'] > 0])

def negative_sentiment_count(df):
    return len(df[df['Sentiment Score'] < 0])

def calculate_sentiment_ratio(positive_count, negative_count):
    if negative_count > 0:
        return positive_count / negative_count
    else:
        return float('inf')
    
def save_df_to_csv(df):
    if not df.empty:
        csv_filename = 'articles.csv'
        df.to_csv(csv_filename, index=False)
        print(f"CSV file '{csv_filename}' has been created successfully.")
    else:
        print("No articles found.")


    



