import pandas as pd
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from transformers import pipeline
import os
from dotenv import load_dotenv

from models.article import Article #transformers library uses advanced machine learning and trained on large text models

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=api_key)

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Calculate the date for yesterday
yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

##### BREAK DOWN THIS FUNCTION (MUCH EASIER TO TEST) ####
def fetch_and_process_query(query, page_size):  # query is the search parameter to retrieve articles by and amount of articles
    #page size must be < 100
    language = 'en'

    # Fetch the news articles from yesterday
    articles = newsapi.get_everything(q=query, language=language, page_size=page_size, from_param=yesterday_date, to=yesterday_date)

    # Check if the request was successful
    if articles['status'] == 'ok':
        # Create a list to store article data
        article_data = []
        
        # Iterate through each article and extract its title, description, and content
        for article in articles['articles']:
            title = article['title']
            description = article['description']
            published_at = article['publishedAt']
            source = article['source'].get('name')
            
            # Combine title and description
            text = f"{title}. {description}"
            
            # Perform sentiment analysis on the combined text
            if text:
                sentiment = sentiment_pipeline(text)
                sentiment_score = sentiment[0]['score'] if sentiment[0]['label'] == 'POSITIVE' else -sentiment[0]['score']
            else:
                sentiment_score = None
            
            # Append article data to the list if sentiment score is within the specified range
            if sentiment_score != 0 and title is not None and description is not None:
                article_data.append({
                    'Published Date': published_at,
                    'Title': title,
                    'Description': description,
                    'Source': source,
                    'Sentiment Score': sentiment_score
                })
        df = pd.DataFrame(article_data)
        # Sort DataFrame by 'Sentiment Score' column
        df_sorted = df.sort_values(by='Sentiment Score', ascending=False)

        return df_sorted
        # Calculate the average sentiment score

############################

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

def top_three_articles(df):
    articles = []
    for idx, row in df.head(3).iterrows():
        title = row['Title']
        description = row['Description']
        published_date = row['Published Date']
        source = row['Source']
        article = Article(None, title, description, published_date, source)
        articles.append(article)
    return articles

def bottom_three_articles(df):
    articles = []
    for idx, row in df.tail(3).iterrows():
        title = row['Title']
        description = row['Description']
        published_date = row['Published Date']
        source = row['Source']
        sentiment = row['Sentiment Score']
        article = Article(None, title, description, published_date, source, sentiment)
        articles.append(article)
    return articles
    

        

### STILL GETTING NULL VALUES IN CSV
### INCLUDE TOTAL ARTICLE COUNT

