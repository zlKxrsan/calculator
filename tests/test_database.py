import os
import sqlite3
import pytest
from app.database import get_db_connection, init_db

# Use a temporary database for testing
TEST_DATABASE = "test_calculator.db"


def test_get_db_connection():
    # Test if the database connection is created successfully
    conn = get_db_connection(TEST_DATABASE)
    try:
        assert isinstance(conn, sqlite3.Connection)
    finally:
        conn.close()

    os.remove(TEST_DATABASE)  # Clean up the test database file


def test_init_db_creates_file_and_table():
    # Test if the database and table are created correctly
    init_db(TEST_DATABASE)
    assert os.path.exists(TEST_DATABASE)  # Database should be created

    # Check if the "calculations" table exists
    conn = get_db_connection(TEST_DATABASE)
    cursor = conn.cursor()
    try:
        result = cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='calculations';"
        ).fetchone()
        assert result is not None  # Table should exist
        assert result[0] == "calculations"  # Table name should match
    finally:
        conn.close()
