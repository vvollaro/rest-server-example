"""Module exposing the route / """
from flask import Blueprint, abort, request

from rest_server_example.user import User

BP = Blueprint("root", __name__)


@BP.route("/")
def root_route():
    """Exposes "/" route."""
    return User("root").hello()

@BP.route("/hello")
def hello_route():
    """Exposes "/hello" route.
    Optional query string name can be given. Must be a string.
    """
    name = request.args.get("name", "world")
    if name.isdigit():
        abort(400)

    return User(name).hello()


@BP.route("/goodbye")
def goodbye_route():
    """Exposes "/goodbye" route.
    Optional query string name can be given. Must be a string.
    """
    name = request.args.get("name", "world")
    if name.isdigit():
        abort(400)
    return User(name).goodbye()
