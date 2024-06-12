from lib.news_fetch_functions import process_article
from unittest.mock import Mock, patch

@patch('lib.news_fetch_functions.sentiment_pipeline') #Horrendous Test to complete
def test_process_article(mock_sentiment_pipeline):
    mock_sentiment_pipeline.return_value = [{'label': 'POSITIVE', 'score': 0.8}]

    article = {
        'title': 'Test Article 1',
        'description': 'Description 1',
        'published at': '2024-06-11T14:08:22Z',
        'source': {'name': 'Source 1'}
    }
    mock_extract_article_info = Mock()
    mock_combine_text = Mock()
    mock_validate_article = Mock()
    mock_analyse_sentiment = Mock()

    mock_extract_article_info.return_value = ('Test Article 1', 'Description 1', '2024-06-11T14:08:22Z', 'Source 1')
    mock_combine_text.return_value = 'title. description'
    mock_validate_article.return_value = True
    mock_analyse_sentiment.return_value = 0.8

    expected_result = {
            'Published Date': '2024-06-11T14:08:22Z',
            'Title': 'Test Article 1',
            'Description': 'Description 1',
            'Source': 'Source 1',
            'Sentiment Score': 0.8
        }
    assert process_article(article) == expected_result


    