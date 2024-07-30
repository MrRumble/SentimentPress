# 📰 SentimentPress 📰


## Description
Don't let the news give you the headline headache! This project aims to simplify the process of fetching headlines from various news sources and analyzing their sentiment.

<div style="padding:48.75% 0 0 0;position:relative;">
  <iframe src="https://player.vimeo.com/video/992234390?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" 
          frameborder="0" 
          allow="autoplay; fullscreen; picture-in-picture; clipboard-write" 
          style="position:absolute;top:0;left:0;width:100%;height:100%;" 
          title="SentimentPress Demo">
  </iframe>
</div>

## Requirements

- NEWSAPI_KEY
- MONGODB_URL
- REDIS_HOST
- REDIS_PORT
- REDIS_DB
- REDIS_TEST_DB
- SECRET_KEY

## Redis Setup

- brew install redis
- set up a production db and test_tb

To switch between production DB and test DB in Redis Insight:
- SELECT 0   <- Production DB
- SELECT 1   <- Test DB

Make sure these are matched in your .env file.

## Performance Imrovements

To speed up the fetch_and_process_query function, which is slow because sentiment analysis is CPU-intensive, I first tried using multiprocessing. But since Hugging Face’s sentiment analysis already uses multiprocessing internally, adding more processes didn’t help much. So, I’ve put fetch_and_process_query back to how it was and put a hold on further performance tweaks for now.
