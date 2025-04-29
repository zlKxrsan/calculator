import pytest
from app.main import app, create_app
from app.database import get_db_connection, init_db
from unittest.mock import patch, MagicMock


@pytest.fixture
def client():
    # Set up Flask test client
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("app.main.get_db_connection")
def test_index_get(mock_get_db_connection, client):
    # Mock the database connection and return an empty history
    mock_conn = MagicMock()
    mock_conn.execute.return_value.fetchall.return_value = []
    mock_get_db_connection.return_value = mock_conn

    # Simulate GET request
    response = client.get("/")
    assert response.status_code == 200
    assert b"History" in response.data  # Check if "History" is in the response


@patch("app.main.get_db_connection")
@patch("app.main.calculate")
def test_index_post(mock_calculate, mock_get_db_connection, client):
    # Mock the calculate function
    mock_calculate.return_value = "42"

    # Mock the database connection
    mock_conn = MagicMock()
    mock_get_db_connection.return_value = mock_conn

    # Simulate a POST request with a valid function
    response = client.post("/", data={"function": "6 * 7"})
    assert response.status_code == 200

    # Verify that the calculation was saved to the database
    mock_conn.execute.assert_any_call(
        "INSERT INTO calculations (function, result) VALUES (?, ?)",
        ("6 * 7", "42"),
    )
    mock_conn.commit.assert_called_once()


# Im Test
@patch("app.main.init_db")
@patch("app.main.app.run")
def test_app_initialization(mock_app_run, mock_init_db):
    app = create_app()  # App initialisieren
    mock_init_db.assert_called_once()  # Überprüfen, dass init_db aufgerufen wurde
    mock_app_run.assert_not_called()  # Überprüfen, dass app.run nicht aufgerufen wurde
