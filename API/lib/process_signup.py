from .database_connection import DatabaseConnection


class SignupProcessor:

    def __init__(self):
        self.database_connection = DatabaseConnection()

    def check_email_exists(self, email):
        db_connection = self.database_connection.get_database()
        return db_connection['users'].find_one({"email": email}) is not None

    def insert_user(self, firstname, lastname, email, password):
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "password": password
        }

        db_connection = self.database_connection.get_database()
        db_connection["users"].insert_one(user)
