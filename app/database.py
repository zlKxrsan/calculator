# database.py
#
# Handles database connection and initialization for the calculator database.
#
# Author: Lawan Mai
# Created: 28.04.2025
# Version: 1.0

import sqlite3
import os

DATABASE = "calculator.db"


# Create a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # So results behave like dicts
    return conn


# Initialize the database (only if it doesn't exist yet)
def init_db():
    if not os.path.exists(DATABASE):
        with get_db_connection() as conn:
            conn.execute(
                """
                CREATE TABLE calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    num1 REAL NOT NULL,
                    num2 REAL NOT NULL,
                    operation TEXT NOT NULL,
                    result TEXT NOT NULL
                )
            """
            )
            conn.commit()
