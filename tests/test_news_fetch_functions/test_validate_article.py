from lib.news_fetch_functions import validate_article

def test_validate_article_true():
    assert validate_article('title', 'description', 0.8) == True

def test_validate_article_none_title_false():
    assert validate_article(None, 'description', 0.8) == False

def test_validate_article_none_description_false():
    assert validate_article('title', None, 0.8) == False

def test_validate_article_sentiment_zero_false():
    assert validate_article('title', 'description', 0) == False

def test_validate_article_none_title_description_false():
    assert validate_article(None, None, 0.8) == False