import pandas as pd

"""
This class converts article data into a pandas dataframe, 
facilitating easy sorting based on sentiment in descending order. 
While it may be considered an unnecessary step, 
it also provides a straightforward method for saving data to CSV, 
which could prove useful in future applications.
"""

# Not tested as only using basic pandas method calls

class DataHandler:
    def create_dataframe(self, article_data):
        return pd.DataFrame(article_data)

    def sort_dataframe(self, df, column='Sentiment Score'):
        return df.sort_values(by=column, ascending=False)

    def save_df_to_csv(self, df, filename='articles.csv'):
        if not df.empty:
            df.to_csv(filename, index=False)
            print(f"CSV file '{filename}' has been created successfully.")
        else:
            print("No articles found.")
