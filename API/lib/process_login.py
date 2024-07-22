from .database_connection import DatabaseConnection
from flask_bcrypt import check_password_hash


class LoginProcessor:

    def __init__(self):
        self.database_connection = DatabaseConnection()

    def email_exists(self, email):
        db_connection = self.database_connection.get_database()
        print(db_connection['users'].find_one({"email": email}))
        return db_connection['users'].find_one({"email": email}) is not None

    def password_is_valid(self, email, password):
        db_connection = self.database_connection.get_database()
        password_hash = db_connection['users'].find_one({"email": email})['password']
        return check_password_hash(password_hash, password)
