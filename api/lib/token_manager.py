from dotenv import load_dotenv
from os import getenv
import jwt

load_dotenv()


class TokenManager:

    def __init__(self):
        self.secret_key = getenv("SECRET_KEY")

    def verify_token(self, token):
        try:
            # Use the JWT_SECRET_KEY directly in token verification
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            return None  # Token has expired
        except jwt.InvalidTokenError:
            return None  # Invalid token
