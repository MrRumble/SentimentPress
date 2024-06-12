from lib.news_fetch_functions import analyse_sentiment
from unittest.mock import patch

@patch('lib.news_fetch_functions.sentiment_pipeline') 
def test_positie_sentiment(mock_sentiment_pipeline):
        #'fake' The sentiment_pipeline()
        mock_sentiment_pipeline.return_value = [{'label': 'POSITIVE', 'score': 0.8}]
        text = "This is a great day!"
        result = analyse_sentiment(text)
        assert result == 0.8

@patch('lib.news_fetch_functions.sentiment_pipeline') 
def test_negative_sentiment(mock_sentiment_pipeline):
        #'fake' The sentiment_pipeline()
        mock_sentiment_pipeline.return_value = [{'label': 'NEGATIVE', 'score': 0.8}]
        text = "This is a bad day!"
        result = analyse_sentiment(text)
        assert result == -0.8

@patch('lib.news_fetch_functions.sentiment_pipeline') 
def test_no_text_input(mock_sentiment_pipeline):        
        text = None
        result = analyse_sentiment(text)
        assert result == None