# main.py
#
# Flask application to run a web-based calculator.
# Handles user input, forwards tasks to the responsible modules, and renders the results.
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
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        # calculate
        result = calculate(num1, num2, operation)

        # Save calculation to the database
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO calculations (num1, num2, operation, result) VALUES (?, ?, ?, ?)",
            (num1, num2, operation, result),
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
