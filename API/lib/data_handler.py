import pandas as pd

#--- This class is used to convert the article data into a pandas dataframe, easier to sort
#--- the data into descending order based on sentiment. Could be argued to be an unnessery step?
#--- On the other hand provides an easy way of saving data to csv, 
# which is not being used in our application as of yet but might be usefuo further down the line

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
