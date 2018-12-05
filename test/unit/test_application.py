""" Unit tests for the Application"""
from unittest.mock import patch

from flask import Flask

from rest_server_example import routes
from rest_server_example.application import Application


@patch.object(Application, "register_blueprint", return_value=None)
@patch.object(Flask, "__init__", return_value=None)
def test_application_init(flask_mock, application_mock):
    """Test Application initialization"""
    app = Application()

    flask_mock.assert_called_once_with(app, "rest_server_example.application")
    application_mock.assert_called_once_with(routes.BP)
