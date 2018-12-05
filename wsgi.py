"""Wsgi module for Apache"""

from rest_server_example.application import Application

application = Application()  # pylint: disable=C0103

if __name__ == "__main__":
    application.run()
