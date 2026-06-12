import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask

load_dotenv(override=True)

app = Flask(__name__)


def get_database_connection():
    """Create and return a connection to the MySQL database."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


@app.route("/")
def home():
    """Return a simple message to confirm that the Flask server is running."""
    return "Campus Lost and Found Platform backend is running."


@app.route("/db-test")
def database_test():
    """Test whether the Flask application can connect to the database."""
    connection = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        cursor.close()

        return {
            "message": "Database connection successful.",
            "tables": tables,
        }

    except mysql.connector.Error as error:
        print(f"Database connection failed: {error}")
        return {
            "message": "Database connection failed. Check the terminal for details."
        }, 500

    finally:
        if connection is not None and connection.is_connected():
            connection.close()