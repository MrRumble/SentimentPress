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

**Purpose**: Contains standalone utility scripts used for administrative tasks, development, or maintenance of the application.

**Files**:
- **`news_category_populator.py`**: Script for populating the database with predefined news categories and adding custom queries. This script is intended for administrative use and will use API calls, so caution is advised.

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
