from lib.news_fetch_functions import fetch_and_process_query

df = fetch_and_process_query('trump', 100)
print(df.head())