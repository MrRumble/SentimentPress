
# This class serves to run some additional useful and interesting analysis on the article dataframe, which will later be bundled with the search object to send to the database.

class SentimentAnalyser:
    def calculate_average_sentiment(self, df):
        return df['Sentiment Score'].mean()

    def calculate_positive_sentiment_count(self, df):
        return len(df[df['Sentiment Score'] > 0])

    def calculate_negative_sentiment_count(self, df):
        return len(df[df['Sentiment Score'] < 0])

    def calculate_sentiment_ratio(self, positive_count, negative_count):
        if negative_count > 0:
            return positive_count / negative_count
        else:
            return float('inf')
