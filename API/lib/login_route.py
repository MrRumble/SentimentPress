from flask import Blueprint, jsonify, request
from flask_cors import CORS
from .process_login import LoginProcessor

login_route = Blueprint('login_route', __name__)
CORS(login_route)


@login_route.route("/login", methods=["POST"])
def login():
    login_processor = LoginProcessor()
    data = request.get_json()
    email = data.get('email', '')

    if not login_processor.email_exists(email):
        return jsonify({"error": "Email does not exist"}), 400

    return jsonify(login_processor.get_hashed_password(email))
