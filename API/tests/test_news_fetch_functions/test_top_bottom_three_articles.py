import pandas as pd
from lib.news_fetch_functions import top_three_articles, bottom_three_articles
from models.article import Article

test_data = {
    'Title': ['Title 1', 'Title 2', 'Title 3', 'Title 4'],
    'Description': ['Description 1', 'Description 2', 'Description 3', 'Description 4'],
    'Published Date': ['2024-06-11T14:08:22Z', '2024-06-12T10:30:00Z', '2024-06-13T08:15:45Z', '2024-06-14T09:20:30Z'],
    'Source': ['Source 1', 'Source 2', 'Source 3', 'Source 4'],
    'Sentiment Score': [0.8, 0.7, 0.9, 0.6]
}

df = pd.DataFrame(test_data)

def test_top_three_articles():
    expected_articles = [
        Article(None, 'Title 3', 'Description 3', '2024-06-13T08:15:45Z', 'Source 3', 0.9),
        Article(None, 'Title 1', 'Description 1', '2024-06-11T14:08:22Z', 'Source 1', 0.8),
        Article(None, 'Title 2', 'Description 2', '2024-06-12T10:30:00Z', 'Source 2', 0.7)
    ]

    top_articles = top_three_articles(df)

    assert len(top_articles) == len(expected_articles) 
    for top_article, expected_article in zip(top_articles, expected_articles):
        assert top_article.title == expected_article.title
        assert top_article.description == expected_article.description
        assert top_article.published_date == expected_article.published_date
        assert top_article.source == expected_article.source
        assert top_article.sentiment == expected_article.sentiment

def test_bottom_three_articles():
    expected_articles = [
        Article(None, 'Title 4', 'Description 4', '2024-06-14T09:20:30Z', 'Source 4', 0.6),
        Article(None, 'Title 2', 'Description 2', '2024-06-12T10:30:00Z', 'Source 2', 0.7),
        Article(None, 'Title 1', 'Description 1', '2024-06-11T14:08:22Z', 'Source 1', 0.8)
    ]

    bottom_articles = bottom_three_articles(df)

    assert len(expected_articles) == len(bottom_articles)
    for bottom_article, expected_article in zip(bottom_articles, expected_articles):
        assert bottom_article.title == expected_article.title
        assert bottom_article.description == expected_article.description
        assert bottom_article.published_date == expected_article.published_date
        assert bottom_article.source == expected_article.source
        assert bottom_article.sentiment == expected_article.sentiment 


    

    
