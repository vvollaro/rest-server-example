"""Unit tests for root routes"""

from unittest.mock import patch

from rest_server_example.user import User


@patch.object(User, "hello", return_value="Hello mock!")
@patch.object(User, "__init__", return_value=None)
def test_root_route(mock_user_init, mock_user_hello, app):
    """Test the route '/'"""

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"Hello mock!"

    mock_user_init.assert_called_once_with("root")
    mock_user_hello.assert_called_once_with()
