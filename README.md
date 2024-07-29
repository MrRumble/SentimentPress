# 📰 SentimentPress 📰


## Description
Don't let the news give you the headline headache! This project aims to simplify the process of fetching headlines from various news sources and analyzing their sentiment.

## Requirements

- NEWSAPI_KEY
- MONGODB_URL
- REDIS_HOST
- REDIS_PORT
- REDIS_DB
- SECRET_KEY

## Redis Setup

- brew install redis

## Performance Imrovements

To speed up the fetch_and_process_query function, which is slow because sentiment analysis is CPU-intensive, I first tried using multiprocessing. But since Hugging Face’s sentiment analysis already uses multiprocessing internally, adding more processes didn’t help much. So, I’ve put fetch_and_process_query back to how it was and put a hold on further performance tweaks for now.
