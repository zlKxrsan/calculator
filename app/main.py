# main.py
#
# Flask application to run a web-based calculator.
# Handles user input, forwards tasks to the responsible modules, and renders the page.
#
# Author: Lawan Mai
# Created: 28.04.2025
# Version: 1.0


from flask import Flask, request, render_template
import sqlite3
import os

from database import get_db_connection, init_db
from calculator import calculate

# Create Flask app
app = Flask(__name__)


# Route: Homepage
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        function = request.form.get("function")

        # calculate
        result = calculate(function)

        # Save calculation to the database
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO calculations (function, result) VALUES (?, ?)",
            (function, result),
        )
        conn.commit()
        conn.close()

    # Fetch calculation history from the database
    conn = get_db_connection()
    history = conn.execute("SELECT * FROM calculations ORDER BY id DESC").fetchall()
    conn.close()

    return render_template("index.html", result=result, history=history)


# run the app
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
