from lib.news_fetch_functions import *

df = fetch_and_process_query('trump', 100)
save_df_to_csv(df)
