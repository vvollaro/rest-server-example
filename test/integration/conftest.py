"""Fixtures for all integration tests for routes"""
from flask import Flask
import pytest

from rest_server_example import routes


@pytest.fixture
def app(scope="session"): # scope used to configure the fixture pylint: disable=W0613
    """Fixture to create the application for the tests"""
    flask_app = Flask(__name__)
    flask_app.register_blueprint(routes.BP)
    flask_app.testing = True

    return flask_app
