import pandas as pd
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from transformers import pipeline #transformers library uses advanced machine learning and trained on large text models

# Initialize News API client with your API key
newsapi = NewsApiClient(api_key='559c8cef5f0440dc919a589056dd603e')

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline('sentiment-analysis')

# Calculate the date for yesterday
yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

def fetch_and_process_query(query):  # query is the search parameter to retrieve articles by

    language = 'en'
    page_size = 100

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
        
        # Create a DataFrame from the article data
        # Set display options to show all rows and columns
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        df = pd.DataFrame(article_data)
        # Sort DataFrame by 'Sentiment Score' column
        df_sorted = df.sort_values(by='Sentiment Score', ascending=False)
        # Calculate the average sentiment score

        average_sentiment = df['Sentiment Score'].mean()

        positive_sentiment_count = len(df[df['Sentiment Score'] > 0])
        negative_sentiment_count = len(df[df['Sentiment Score'] < 0])

        # Calculate the ratio of positive to negative sentiment rows
        if negative_sentiment_count > 0:
            ratio = positive_sentiment_count / negative_sentiment_count
        else:
            ratio = float('inf')  # To handle cases where there are no negative sentiment rows

        # Print useful data about the query

        print("Number of rows with positive sentiment:", positive_sentiment_count)
        print("Number of rows with negative sentiment:", negative_sentiment_count)
        print("Ratio of positive to negative sentiment rows:", ratio)
        print(f'The average sentiment score for {yesterday_date}, in the category {query}, was {average_sentiment}')

        print("Top 3 Articles:")
        for idx, row in df_sorted.head(3).iterrows():
            print(f"Title: {row['Title']}")
            print(f"Description: {row['Description']}")
            print(f"Source: {row['Source']}")
            print("\n")

        print("\nBottom 3 Articles:")
        for idx, row in df_sorted.tail(3).iterrows():
            print(f"Title: {row['Title']}")
            print(f"Description: {row['Description']}")
            print(f"Source: {row['Source']}")
            print("\n")


        # Write the DataFrame to a CSV file if it has rows
        # if not df.empty:
        #     csv_filename = f'{query}_articles_{yesterday_date}.csv'
        #     df.to_csv(csv_filename, index=False)
        #     print(f"CSV file '{csv_filename}' has been created successfully.")
        # else:
        #     print("No articles found.")
    else:
        # Print an error message if the request was not successful
        print("Failed to fetch news articles. Check your API key or try again later.")



### MAYBE JUST FOR UK NEWS?
### STILL GETTING NULL VALUES IN CSV
### INCLUDE TOTAL ARTOCE COUNT
