from .redis_connection import RedisConnection


def add_to_blacklist(jti, expires_at=30):  # Expiry time is in SECONDS
    with RedisConnection() as red_conn:
        red_conn.set(jti, '', ex=expires_at)


def is_blacklisted(jti):
    with RedisConnection() as red_conn:
        return red_conn.get(jti) is not None