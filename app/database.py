# database.py
#
# Handles database connection and initialization for the calculator database.
#
# Author: Lawan Mai
# Created: 28.04.2025
# Version: 1.2

import sqlite3
import os

DATABASE = "calculator.db"


# Create a database connection
def get_db_connection(db_path=None):
    path = (
        db_path or DATABASE
    )  # provides a way to override the database path for testing
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row  # Allows accessing like a dictionary
    return conn


# Initialize the database (only if it doesn't exist yet)
def init_db(db_path=None):
    path = (
        db_path or DATABASE
    )  # provides a way to override the database path for testing
    if not os.path.exists(path):
        with get_db_connection(db_path) as conn:
            conn.execute(
                """
                CREATE TABLE calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    function TEXT NOT NULL,
                    result TEXT NOT NULL
                )
                """
            )
            conn.commit()
