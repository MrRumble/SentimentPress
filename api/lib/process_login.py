import uuid
from datetime import timedelta
from typing import Optional
from flask_bcrypt import check_password_hash
from flask_jwt_extended import create_access_token
from dotenv import load_dotenv
from api.lib.database_connection import DatabaseConnection

load_dotenv()


class LoginProcessor:
    def __init__(self):
        self.db = DatabaseConnection().get_database()
        self.users_collection = self.db['users']

    def get_user_by_email(self, email: str) -> Optional[dict]:
        try:
            return self.users_collection.find_one({"email": email})
        except Exception as e:
            print(f"Database error: {e}")
            raise

    def email_exists(self, email: str) -> bool:
        user = self.get_user_by_email(email)
        print(f"User found: {user}")
        return user is not None

    def password_is_valid(self, email: str, password: str) -> bool:
        user = self.get_user_by_email(email)
        if not user or 'password' not in user:
            return False
        return check_password_hash(user['password'], password)

    def generate_jwt(self, email: str) -> str:
        user = self.get_user_by_email(email)
        if not user:
            raise ValueError("User not found")

        user_id = str(user['_id'])
        token_id = str(uuid.uuid4())

        token = create_access_token(
            identity=user_id,
            additional_claims={'jti': token_id},
            expires_delta=timedelta(minutes=30)  # Fix this so it works with JWT_ACCESS_TOKEN_EXPIRES in .env
        )
        return token

    def package_user_details(self, email: str) -> dict:
        user = self.get_user_by_email(email)

        if not user:
            raise ValueError("User not found")

        first_name = user.get('firstname', '')
        last_name = user.get('lastname', '')
        user_details = {
            'first_name': first_name,
            'last_name': last_name
        }

        return user_details
