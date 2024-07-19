from .database_connection import DatabaseConnection


class LoginProcessor:

    def __init__(self):
        self.database_connection = DatabaseConnection()

    def email_exists(self, email):
        db_connection = self.database_connection.get_database()
        print(db_connection['users'].find_one({"email": email}))
        return db_connection['users'].find_one({"email": email}) is not None

    def get_hashed_password(self, email):
        db_connection = self.database_connection.get_database()
        return db_connection['users'].find_one({"email": email})['password']
