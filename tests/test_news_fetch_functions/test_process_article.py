from lib.news_fetch_functions import process_article
from unittest.mock import Mock, patch

@patch('lib.news_fetch_functions.extract_article_info')
@patch('lib.news_fetch_functions.sentiment_pipeline')
def test_process_article( mock_sentiment_pipeline, mock_extract_article_info):
    mock_sentiment_pipeline.return_value = [{'label': 'POSITIVE', 'score': 0.8}]

    article = {
        'title': 'Test Article 1',
        'description': 'Description 1',
        'publishedAt': '2024-06-11T14:08:22Z',
        'source': {'name': 'Source 1'}
    }
    
    mock_extract_article_info.return_value = ('Test Article 1', 'Description 1', '2024-06-11T14:08:22Z', 'Source 1')

    expected_result = {
        'Published Date': '2024-06-11T14:08:22Z',
        'Title': 'Test Article 1',
        'Description': 'Description 1',
        'Source': 'Source 1',
        'Sentiment Score': 0.8
    }
    assert process_article(article) == expected_result


    