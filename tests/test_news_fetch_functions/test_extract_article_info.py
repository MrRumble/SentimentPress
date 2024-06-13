from lib.news_fetch_functions import extract_article_info, combine_text
from datetime import datetime, timedelta
from unittest.mock import patch
import pytest

yesterday_date = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

def test_extract_article_info_correct():
    article = {
        'title': 'Test Article 1',
        'description': 'Description 1',
        'publishedAt': '2024-06-11T14:08:22Z',
        'source': {'name': 'Source 1'}
    }
    expected_result = ("Test Article 1", "Description 1", '2024-06-11T14:08:22Z', 'Source 1')
    assert extract_article_info(article) == expected_result

def test_combine_text():
    title = 'title'
    description = 'description'
    assert combine_text(title, description) == 'title. description'