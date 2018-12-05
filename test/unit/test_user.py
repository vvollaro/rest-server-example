""" Unit tests for the User"""
from rest_server_example.user import User

def test_hello():
    """Test hello"""
    assert User("test").hello() == "Hello test!"

def test_goodbye():
    """Test hello"""
    assert User("test").goodbye() == "Goodbye test!"
