from .redis_connection import RedisConnection


def add_to_blacklist(jti, expires_at=30, use_test_db=False):  # Expiry time is in SECONDS
    with RedisConnection(use_test_db=use_test_db) as red_conn:
        red_conn.set(jti, '', ex=expires_at)


def is_blacklisted(jti, use_test_db=False):
    with RedisConnection(use_test_db=use_test_db) as red_conn:
        return red_conn.get(jti) is not None
