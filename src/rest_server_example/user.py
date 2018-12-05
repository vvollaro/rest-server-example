"""Module containing the User class"""

class User(object):
    """Class representing a user"""

    def __init__(self, name):
        """Init of User"""
        self.name = name

    def hello(self):
        """Say hello to the user"""
        return "Hello %s!" % self.name

    def goodbye(self):
        """Say goodbye to the user"""
        return "Goodbye %s!" % self.name
