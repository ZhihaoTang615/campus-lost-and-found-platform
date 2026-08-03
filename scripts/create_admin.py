"""Create an administrator account using the repository's MySQL settings."""

from getpass import getpass
import os
from pathlib import Path
import re

from dotenv import load_dotenv
import mysql.connector
from werkzeug.security import generate_password_hash


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def load_database_config():
    """Load and return the same MySQL settings used by the Flask application."""
    load_dotenv(dotenv_path=ENV_PATH)

    environment_names = ("DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME")
    missing_names = [name for name in environment_names if os.getenv(name) is None]
    if missing_names:
        names = ", ".join(missing_names)
        raise ValueError(f"Missing database configuration: {names}")

    return {
        "host": os.getenv("DB_HOST"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "database": os.getenv("DB_NAME"),
    }


def prompt_for_account_details():
    """Prompt for and validate administrator account details."""
    full_name = input("Full name: ").strip()
    email = input("Email: ").strip().lower()
    password = getpass("Password: ")
    password_confirmation = getpass("Confirm password: ")

    if not full_name:
        raise ValueError("Full name is required.")
    if len(full_name) > 100:
        raise ValueError("Full name must be 100 characters or fewer.")
    if not email or not EMAIL_PATTERN.fullmatch(email):
        raise ValueError("Enter a valid email address.")
    if len(email) > 150:
        raise ValueError("Email must be 150 characters or fewer.")
    if not password or not password.strip():
        raise ValueError("Password is required.")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    if password != password_confirmation:
        raise ValueError("Passwords do not match.")

    return full_name, email, password


def create_admin_account(full_name, email, password, database_config):
    """Insert one password-hashed administrator account."""
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(**database_config)
        cursor = connection.cursor()
        password_hash = generate_password_hash(password)

        cursor.execute(
            """
            INSERT INTO users (full_name, email, password_hash, role)
            VALUES (%s, %s, %s, %s)
            """,
            (full_name, email, password_hash, "admin"),
        )
        connection.commit()
    except mysql.connector.IntegrityError:
        print("An account with that email address already exists.")
        return False
    except mysql.connector.Error:
        print("The administrator account could not be created due to a database error.")
        return False
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

    print("Administrator account created successfully.")
    return True


def main():
    """Run the interactive administrator-account creation workflow."""
    try:
        database_config = load_database_config()
        full_name, email, password = prompt_for_account_details()
    except ValueError as error:
        print(error)
        return 1
    except (EOFError, KeyboardInterrupt):
        print("\nAdministrator account creation cancelled.")
        return 1

    was_created = create_admin_account(
        full_name,
        email,
        password,
        database_config,
    )
    return 0 if was_created else 1


if __name__ == "__main__":
    raise SystemExit(main())
