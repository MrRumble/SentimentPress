from .database_connection import DatabaseConnection
from flask_bcrypt import Bcrypt


class SignupProcessor:

    def __init__(self):
        self.database_connection = DatabaseConnection()

    def check_email_exists(self, email):
        db_connection = self.database_connection.get_database()
        return db_connection['users'].find_one({"email": email}) is not None

    def insert_user(self, firstname, lastname, email, password):
        bcrypt = Bcrypt()
        hashed_password = bcrypt.generate_password_hash(password, 12).decode('utf-8')

        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": hashed_password
        }

        db_connection = self.database_connection.get_database()
        db_connection["users"].insert_one(user)
