from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager
from api.lib.routes.query_route import query_route
from api.lib.routes.signup_route import signup_route
from api.lib.routes.login_route import login_route
from api.lib.routes.logout_route import logout_route

load_dotenv()

# Create a new Flask app
app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = os.getenv('JWT_ACCESS_TOKEN_EXPIRES')
jwt = JWTManager(app)

app.register_blueprint(query_route)
app.register_blueprint(signup_route)
app.register_blueprint(login_route)
app.register_blueprint(logout_route)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5002)))