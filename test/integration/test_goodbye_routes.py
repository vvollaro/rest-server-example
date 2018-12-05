"""Unit tests for goodbye routes"""

from unittest.mock import patch

from rest_server_example.user import User


@patch.object(User, "goodbye", return_value="goodbye mock!")
@patch.object(User, "__init__", return_value=None)
def test_goodbye_route_no_param(mock_user_init, mock_user_goodbye, app):
    """Test the route 'goodbye' without parameters"""

    with app.test_client() as client:
        response = client.get("/goodbye")
        assert response.status_code == 200
        assert response.data == b"goodbye mock!"

    mock_user_init.assert_called_once_with("world")
    mock_user_goodbye.assert_called_once_with()

@patch.object(User, "goodbye", return_value="goodbye mock!")
@patch.object(User, "__init__", return_value=None)
def test_goodbye_route_valid_param(mock_user_init, mock_user_goodbye, app):
    """Test the route 'goodbye' without parameters"""

    with app.test_client() as client:
        response = client.get("/goodbye", query_string={"name": "user"})
        assert response.status_code == 200
        assert response.data == b"goodbye mock!"

    mock_user_init.assert_called_once_with("user")
    mock_user_goodbye.assert_called_once_with()

@patch.object(User, "goodbye", return_value="goodbye mock!")
@patch.object(User, "__init__", return_value=None)
def test_goodbye_route_invalid_param(mock_user_init, mock_user_goodbye, app):
    """Test the route 'goodbye' without parameters"""

    with app.test_client() as client:
        response = client.get("/goodbye", query_string={"name": 1})
        assert response.status_code == 400

    mock_user_init.assert_not_called()
    mock_user_goodbye.assert_not_called()
