from models.article import Article

def test_article_format_nice_string():
    test_article = Article(1, "title", "description", "10-10-2010", "source", 0.5)
    assert str(test_article) == "Article(1, title, description, 10-10-2010, source, 0.5)"

def test_same_articles_are_equal():
    test_article1 = Article(1, "title", "description", "10-10-2010", "source", 0.5)
    test_article2 = Article(1, "title", "description", "10-10-2010", "source", 0.5)
    assert test_article1 == test_article2