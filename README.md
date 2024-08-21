# 📰 SentimentPress 📰


## Description
Don't let the news give you the headline headache! This project aims to simplify the process of fetching headlines from various news sources and analyzing their sentiment.

## Requirements

- NEWSAPI_KEY
- MONGODB_URL
- REDIS_HOST
- REDIS_PORT
- REDIS_DB
- REDIS_TEST_DB
- SECRET_KEY

# Project Backend Overview

## Directory Structure

This project is organised into several directories to separate core components, route handlers, data processors, and utility scripts. Below is a brief overview of each directory and its purpose:

### `core/`

**Purpose**: Contains the core components and utilities of the application, such as data handling, database connections, and token management.

**Files**:
- **`data_handler.py`**: Contains general data handling functions.
- **`database_connection.py`**: Manages database connection setup and management.
- **`redis_connection.py`**: Handles Redis connection setup.
- **`redis_manager.py`**: Manages operations related to Redis.
- **`token_manager.py`**: Includes functions related to token creation and validation.
- **`generate_secret_key.py`**: Script for generating a secret key.
- **`query_cache_manager.py`**: Manages the caching of query results. This class handles checking if a query has been processed and cached for the current day, thereby bypassing the need for a fresh API call if a cached result is available. It formats cached results into a structured response format to be used in the application.


### `routes/`

**Purpose**: Houses route handlers or endpoints for the web application.

**Files**:
- **`login_route.py`**: Manages login requests.
- **`logout_route.py`**: Handles logout requests.
- **`query_route.py`**: Deals with query-related requests.
- **`signup_route.py`**: Manages signup requests.
- **`process_login.py`**: Contains logic for processing login requests.
- **`process_signup.py`**: Contains logic for processing signup requests.

### `processors/`

**Purpose**: Contains modules responsible for processing data, including fetching news, summarising articles, and analysing sentiment.

**Files**:
- **`article_processor.py`**: Processes article data.
- **`article_summariser.py`**: Summarises articles.
- **`news_fetcher.py`**: Fetches news data.
- **`news_processor.py`**: Processes news data.
- **`process_query.py`**: Contains logic for processing queries.
- **`sentiment_analyser.py`**: Analyses sentiment in text.

### `scripts/`

# Table Design:
# Search Result Data

| **Field**                      | **Value (Data Type)**                |
|--------------------------------|--------------------------------------|
| **_id**                        | `ObjectId`                            |
| **search_term**                | `string`                              |
| **search_date**                | `ISO8601 datetime`                    |
| **sentiment_score**            | `float`                               |
| **positive_article_count**     | `integer`                             |
| **negative_article_count**     | `integer`                             |
| **total_article_count**        | `integer`                             |
| **ratio_positive_vs_negative** | `float`                               |
| **main_headline**              | `string`                              |
| **top_3_articles**             | `Array of Objects`                    |
| **bottom_3_articles**             | `Array of Objects`                    |

### Top 3 Articles

These articles are sorted based on their sentiment score:

| **Index** | **Field**         | **Value (Data Type)**                |
|-----------|-------------------|--------------------------------------|
| **0**     | **Object**        |                                      |
|           | title             | `string`                              |
|           | description       | `string`                              |
|           | published_date    | `ISO8601 datetime`                    |
|           | source            | `string`                              |
|           | sentiment         | `float`                               |
| **1**     | **Object**        |                                      |
|           | title             | `string`                              |
|           | description       | `string`                              |
|           | published_date    | `ISO8601 datetime`                    |
|           | source            | `string`                              |
|           | sentiment         | `float`                               |
| **2**     | **Object**        |                                      |
|           | title             | `string`                              |
|           | description       | `string`                              |
|           | published_date    | `ISO8601 datetime`                    |
|           | source            | `string`                              |
|           | sentiment         | `float`                               |

### Bottom 3 Articles

| **Index** | **Field**         | **Value (Data Type)**                |
|-----------|-------------------|--------------------------------------|
| **0**     | **Object**        |                                      |
|           | title             | `string`                              |
|           | description       | `string`                              |
|           | published_date    | `ISO8601 datetime`                    |
|           | source            | `string`                              |
|           | sentiment         | `float`                               |
| **1**     | **Object**        |                                      |
|           | title             | `string`                              |
|           | description       | `string`                              |
|           | published_date    | `ISO8601 datetime`                    |
|           | source            | `string`                              |
|           | sentiment         | `float`                               |
| **2**     | **Object**        |                                      |
|           | title             | `string`                              |
|           | description       | `string`                              |
|           | published_date    | `ISO8601 datetime`                    |
|           | source            | `string`                              |
|           | sentiment         | `float`                               |


# Search Metadata

| **Field**        | **Value (Data Type)** |
|------------------|------------------------|
| **_id**          | `ObjectId`             |
| **search_date**  | `string` (Date)        |
| **search_time**  | `string` (Time)        |
| **search_id**    | `string`               |
| **search_term**  | `string`               |
| **user_id**      | `string` or `null`     |

### Note
- **user_id**: Can be a `string` or `null` if no user ID is assigned.

# User Data Table Design

| Field        | Data Type | Description                              |
|--------------|-----------|------------------------------------------|
| `_id`        | ObjectId  | Unique identifier for the user           |
| `username`   | String    | User's login name                        |
| `first_name` | String    | User's first name                        |
| `last_name`  | String    | User's last name                         |
| `email`      | String    | User's email address                     |
| `password`   | String    | User's password (masked)                 |

# Analysis of Search Data

## 1. Analysing Popular Searches

### Search Term Analysis

- **Frequency Analysis:** By aggregating data based on `search_term`, you can identify which search terms are most frequently queried. This helps in understanding current trends or topics of interest.
- **Trend Analysis:** Track how search terms vary over time. For example, you might analyse how the frequency of certain search terms changes over weeks or months.

### Temporal Patterns

- **Date and Time Analysis:** By examining `search_date` and `search_time`, you can identify peak search times and days. This helps in scheduling content or optimising server load.
- **Seasonal Trends:** Analyse whether certain search terms spike during particular times of the year. For instance, political events might increase searches related to specific politicians.

## 2. Gaining Insights

### User Behaviour

- **User Engagement:** While the `user_id` is `null` in this case, if present, it can help track which users are performing searches. This can be used to segment users based on their search behaviours.
- **Personalisation:** By associating searches with user IDs, you can tailor content recommendations based on previous search patterns of individual users.

### Search Performance

- **Search ID Tracking:** Each search has a unique `search_id`, which helps in tracking and analysing the results of specific searches. This can be useful for debugging, auditing, and improving search functionalities.

### Contextual Analysis

- **Search Term Context:** Analyse the context or associated content of popular search terms to provide deeper insights into why certain topics are trending. This might involve connecting search terms with articles or news content.




## Usage

Ensure that you have the necessary packages installed and properly configured. You can run the application using the main entry point of the project, typically specified in the `__init__.py` files or another startup script.

Feel free to explore the directories and files to understand the structure and functionality of the backend. Each component is designed to handle specific tasks, contributing to a modular and organised codebase.


## Usage

Ensure that you have the necessary packages installed and properly configured. You can run the application using the main entry point of the project, typically specified in the `__init__.py` files or another startup script.

Feel free to explore the directories and files to understand the structure and functionality of the backend. Each component is designed to handle specific tasks, contributing to a modular and organized codebase.


## Redis Setup

- brew install redis
- set up a production db and test_tb

To switch between production DB and test DB in Redis Insight:
- SELECT 0   <- Production DB
- SELECT 1   <- Test DB

Make sure these are matched in your .env file.

## Performance Imrovements

To speed up the fetch_and_process_query function, which is slow because sentiment analysis is CPU-intensive, I first tried using multiprocessing. But since Hugging Face’s sentiment analysis already uses multiprocessing internally, adding more processes didn’t help much. So, I’ve put fetch_and_process_query back to how it was and put a hold on further performance tweaks for now.
