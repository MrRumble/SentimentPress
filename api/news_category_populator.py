from lib.process_query import QueryProcessor
import time

"""
This class is for admin use only. Run this file from the terminal to populate the database, 
with our pre determined keywords. It also gives the option to quickly insert other keywords into the
database. CAUTION: Running this file will eat into your NewsAPI allowance. 
"""


class NewsCategoryPopulator:
    def __init__(self, categories):
        self.categories = categories
        self.processor = QueryProcessor()

    def populate_database(self):
        start_time = time.time()  # Record start time
        print("Populating the database with predefined news categories...")
        for category in self.categories:
            print(f"Populating: {category}...")
            _, search_result = self.processor.process_query(category, 'ADMIN_JAMES')
            self.processor.save_search_result_to_db(search_result)
        end_time = time.time()  # Record end time
        duration = end_time - start_time
        print(f"Database population completed in {duration:.2f} seconds.")

    def add_custom_query(self):
        custom_query = input("Enter the custom query: ")
        start_time = time.time()
        _, search_result = self.processor.process_query(custom_query, 'ADMIN')
        self.processor.save_search_result_to_db(search_result)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Custom query '{custom_query}' processed and saved to the database in {duration:.2f} seconds.")

    def run(self):
        print("Choose an option:")
        print("1. Populate the database with all news categories (CAUTION: Uses 40+ api calls!)")
        print("2. Add a custom query")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            self.populate_database()
        elif choice == '2':
            self.add_custom_query()
        else:
            print("Invalid choice. Please enter 1 or 2.")


# ------------- python news_category_populator.py -------------- #

news_categories = [
    "World", "Politics", "Business", "Technology", "Science", "Health", "Sports",
    "Entertainment", "Lifestyle", "Education", "Environment", "Travel", "Culture",
    "Opinion", "Local", "National", "International", "Finance", "Real Estate",
    "Automotive", "Food", "Arts", "Music", "Movies", "Television", "Social Media",
    "Gaming", "Cryptocurrency", "Legal", "History", "Religion", "Weather", "Crime",
    "Military", "Fashion", "Celebrity", "Technology", "Startup", "Trump", "Biden"
]

populator = NewsCategoryPopulator(news_categories)
populator.run()
