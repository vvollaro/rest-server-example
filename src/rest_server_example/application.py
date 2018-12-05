"""Entry point for the REST server"""

from flask import Flask
from rest_server_example import routes

class Application(Flask):
    """Start the server"""

    def __init__(self):
        Flask.__init__(self, __name__)
        self.register_blueprint(routes.BP)
