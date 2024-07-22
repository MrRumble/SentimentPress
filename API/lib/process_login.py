from .database_connection import DatabaseConnection
from flask_bcrypt import check_password_hash


class LoginProcessor:

    def __init__(self):
        self.database_connection = DatabaseConnection()

    def email_exists(self, email):
        try:
            db_connection = self.database_connection.get_database()
            user = db_connection['users'].find_one({"email": email})
            print(f"User found: {user}")
            return user is not None

        except Exception as e:
            print(f"Error checking email existence: {str(e)}")
            raise

    def password_is_valid(self, email, password):
        try:
            db_connection = self.database_connection.get_database()
            user = db_connection['users'].find_one({"email": email})
            if user and 'password' in user:
                password_hash = user['password']
                return check_password_hash(password_hash, password)
            return False
        except Exception as e:
            print(f"Error checking password validity: {str(e)}")
            raise
