from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

# Create a new Flask app
app = Flask(__name__)
CORS(app)

# Import the blueprint from query_route after app creation
from lib.query_route import *

app.register_blueprint(query_route)
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5002)))
