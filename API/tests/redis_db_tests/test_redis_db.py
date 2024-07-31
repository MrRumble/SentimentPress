from API.lib.redis_connection import RedisConnection
from API.lib.redis_manager import add_to_blacklist, is_blacklisted
import requests
import pytest

def test_connection_to_test_db():
    """
    Test if a connection to the Redis test database can be established and
    perform basic operations of setting and getting a key.
    """
    with RedisConnection(use_test_db=True) as redis_connection:
        test_key = 'test_key'
        test_value = 'test_value'
        redis_connection.set(test_key, test_value)
        retrieved_value = redis_connection.get(test_key)
        assert retrieved_value == test_value
        redis_connection.delete(test_key)

def test_add_to_blacklist():
    """
    Test that when the add_to_blacklist function is called,
    The jti added is present in the test_db
    """
    with RedisConnection(use_test_db=True) as redis_connection:
        jti = "test_jti"
        add_to_blacklist(jti, use_test_db=True)
        retrieved_value = redis_connection.get(jti)
        assert retrieved_value is not None
        redis_connection.delete(jti)

def test_is_blacklisted_returns_true_if_in_db():
    """
    If a key: value is in the database -> is_blacklisted -> True
        else is_blacklisted -> False
    """
    with RedisConnection(use_test_db=True) as redis_connection:
        test_key = 'test_key'
        test_value = 'test_value'
        redis_connection.set(test_key, test_value)
        result = is_blacklisted(test_key, use_test_db=True)
        false_result = is_blacklisted("Some key not in db", use_test_db=False)
        assert result is True
        assert false_result is False
        redis_connection.delete(test_key)

