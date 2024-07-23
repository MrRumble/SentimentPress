from API.lib.news_fetcher import NewsFetcher
from datetime import datetime, timedelta
from unittest.mock import patch
import pytest

yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')


# A patch is used to mock "get_everything" method from newsapi client.
@patch('API.lib.news_fetcher.NewsApiClient.get_everything')
def test_fetch_articles_successful(mock_get_everything):
    query = "test"
    page_size = 10
    language = 'en'

    mock_response = {
        'status': 'ok',
        'articles': [
            {'title': 'Test Article 1', 'description': 'Description 1'},
            {'title': 'Test Article 2', 'description': 'Description 2'}
        ]
    }
    mock_get_everything.return_value = mock_response
    fetcher = NewsFetcher()
    articles = fetcher.fetch_articles(query, page_size, language, yesterday_date, yesterday_date)
    assert articles == mock_response['articles']


@patch('API.lib.news_fetcher.NewsApiClient.get_everything')
def test_fetch_articles_fails(mock_get_everything):
    query = "test"
    page_size = 10
    language = 'en'

    mock_response = {
        'status': 'error',
        'articles': []
    }
    mock_get_everything.return_value = mock_response
    fetcher = NewsFetcher()
    with pytest.raises(ValueError) as e:
        fetcher.fetch_articles(query, page_size, language, yesterday_date, yesterday_date)
    error_message = str(e.value)
    assert error_message == "Failed to fetch news articles. Check your API key or try again later."
