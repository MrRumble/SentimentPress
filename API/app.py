from lib.news_fetch_functions import *
from flask import Flask
from flask_cors import CORS


load_dotenv()
# Create a new Flask app
app = Flask(__name__)
CORS(app)

from routes.query_route import *

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5002)))
# df = fetch_and_process_query('trump', 100)

# print(df)
