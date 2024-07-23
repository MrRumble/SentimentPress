from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from flask_jwt_extended import JWTManager

load_dotenv()

# Create a new Flask app
app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
jwt = JWTManager(app)

# Import the blueprint from query_route after app creation
from lib.query_route import *
from lib.signup_route import *
from lib.login_route import *

app.register_blueprint(query_route)
app.register_blueprint(signup_route)
app.register_blueprint(login_route)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5002)))
