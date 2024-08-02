from flask import Blueprint, jsonify, request
from flask_cors import CORS
from api.lib.routes.process_login import LoginProcessor

login_route = Blueprint('login_route', __name__)
CORS(login_route)


@login_route.route("/login", methods=["POST"])
def login():
    try:
        login_processor = LoginProcessor()
        data = request.get_json()
        email = data.get('email', '')
        password = data.get('password', '')

        if not login_processor.email_exists(email):
            return jsonify({"error": "Email does not exist"}), 400

        if not login_processor.password_is_valid(email, password):
            return jsonify({"error": "Invalid password"}), 400
        token = login_processor.generate_jwt(email)
        user_details = login_processor.package_user_details(email)
        return jsonify({'token': token, 'user_details': user_details}), 200

    except Exception as e:
        print(f"Login error: {str(e)}")
        return jsonify({"error": str(e)}), 500
