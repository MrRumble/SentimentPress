from flask import Blueprint, jsonify, request
from flask_cors import CORS
from api.lib.redis_manager import add_to_blacklist
from flask_jwt_extended import get_jti

logout_route = Blueprint('logout_route', __name__)
CORS(logout_route)


@logout_route.route("/logout", methods=["POST"])
def logout():
    try:
        data = request.get_json()
        binary_data = data['jti'].encode('utf-8')
        if data is None:
            return jsonify({"error": "No JSON data received"}), 400

        jti = get_jti(binary_data)

        if not jti:
            return jsonify({"error": "Invalid token"}), 400

        add_to_blacklist(jti, 30)
        return jsonify({"message": "Successfully logged out"}), 200

    except Exception as e:
        print(f"Error during logout: {str(e)}")  # Log the error
        return jsonify({"error": "An error occurred during logout"}), 500
