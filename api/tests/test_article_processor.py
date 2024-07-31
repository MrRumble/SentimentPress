from api.lib.article_processor import ArticleProcessor
from datetime import datetime, timedelta
from unittest.mock import patch, MagicMock
import pytest

yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

"""
Unit tested, each method in the ArticleProcessor class.
Finished with a Class-Level test.
"""


def test_extract_article_info_correct():
    processor = ArticleProcessor()
    article = {
        'title': 'Test Article 1',
        'description': 'Description 1',
        'publishedAt': '2024-06-11T14:08:22Z',
        'source': {'name': 'Source 1'}
    }
    expected_result = ("Test Article 1", "Description 1", '2024-06-11T14:08:22Z', 'Source 1')
    assert processor.extract_article_info(article) == expected_result


def test_combine_text():
    processor = ArticleProcessor()
    title = 'title'
    description = 'description'
    assert processor.combine_text(title, description) == 'title. description'


@patch('api.lib.article_processor.pipeline')
def test_analyse_sentiment_positive(mock_pipeline):
    mock_sentiment = MagicMock(return_value=[{'label': 'POSITIVE', 'score': 0.9}])
    mock_pipeline.return_value = mock_sentiment
    processor = ArticleProcessor()
    processor.sentiment_pipeline = mock_pipeline()
    text = "I love this!"
    result = processor.analyse_sentiment(text)
    assert result == 0.9


@patch('api.lib.article_processor.pipeline')
def test_analyse_sentiment_negative(mock_pipeline):
    mock_sentiment = MagicMock(return_value=[{'label': 'NEGATIVE', 'score': 0.8}])
    mock_pipeline.return_value = mock_sentiment
    processor = ArticleProcessor()
    processor.sentiment_pipeline = mock_pipeline()
    text = "I hate this!"
    result = processor.analyse_sentiment(text)
    assert result == -0.8


def test_analyse_sentiment_empty_text():
    processor = ArticleProcessor()
    text = ""
    result = processor.analyse_sentiment(text)
    assert result is None


def test_analyse_sentiment_none_text():
    processor = ArticleProcessor()
    text = None
    result = processor.analyse_sentiment(text)
    assert result is None


def test_validate_article_true():
    processor = ArticleProcessor()
    assert processor.validate_article('title', 'description', 0.8) is True


def test_validate_article_none_title_false():
    processor = ArticleProcessor()
    assert processor.validate_article(None, 'description', 0.8) is False


def test_validate_article_none_description_false():
    processor = ArticleProcessor()
    assert processor.validate_article('title', None, 0.8) is False


def test_validate_article_sentiment_zero_false():
    processor = ArticleProcessor()
    assert processor.validate_article('title', 'description', 0) is False


def test_validate_article_none_title_description_false():
    processor = ArticleProcessor()
    assert processor.validate_article(None, None, 0.8) is False


def test_validate_article_removed_returns_false():
    processor = ArticleProcessor()
    assert processor.validate_article('[Removed]', '[Removed]', 0.8) is False


# -------- Class level test for process_article (uses every other method)

def test_process_article_valid_article():
    processor = ArticleProcessor()
    article = {
        'title': 'Test Article 1',
        'description': 'Description 1',
        'publishedAt': '2024-06-11T14:08:22Z',
        'source': {'name': 'Source 1'}
    }

    processor.extract_article_info = MagicMock(
        return_value=("Test Title", "Test Description", "2024-06-11T14:08:22Z", "Test Source"))
    processor.combine_text = MagicMock(return_value="title. description")
    processor.analyse_sentiment = MagicMock(return_value=0.9)
    processor.validate_article = MagicMock(return_value=True)

    expected_result = {
        'Published Date': "2024-06-11T14:08:22Z",
        'Title': "Test Title",
        'Description': "Test Description",
        'Source': "Test Source",
        'Sentiment Score': 0.9
    }

    assert processor.process_article(article) == expected_result
