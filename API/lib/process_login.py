import os
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from flask_bcrypt import check_password_hash
from dotenv import load_dotenv
from .database_connection import DatabaseConnection

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')


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

        payload = {
            'user_id': str(user['_id']),
            'exp': datetime.now(timezone.utc) + timedelta(minutes=30)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        print(f"Generated JWT: {token}")
        return token
