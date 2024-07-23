import redis
from dotenv import load_dotenv
import os

load_dotenv()


class RedisConnection:
    def __init__(self,
                 host=os.environ.get("REDIS_HOST"),
                 port=os.environ.get("REDIS_PORT"),
                 db=os.environ.get("REDIS_DB")):
        self.host = host
        self.port = port
        self.db = db
        self.connection = None

    def __enter__(self):
        self.connection = redis.StrictRedis(
            host=self.host, port=self.port, db=self.db, decode_responses=True
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
