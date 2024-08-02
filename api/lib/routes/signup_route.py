from flask import Blueprint, jsonify, request
from flask_cors import CORS
from api.lib.routes.process_signup import SignupProcessor

signup_route = Blueprint('signup_route', __name__)
CORS(signup_route)


@signup_route.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    firstname = data.get('firstName', '')
    lastname = data.get('lastName', '')
    email = data.get('email', '')
    password = data.get('password', '')

    # Perform signup processing here
    signup_processor = SignupProcessor()
    if signup_processor.check_email_exists(email):
        return jsonify({"error": "Email already exists"}), 400
    else:
        signup_processor.insert_user(firstname, lastname, email, password)
        return jsonify("Signup successful!"), 200
