import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

load_dotenv(dotenv_path=".env", override=True)

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")


def get_database_connection():
    """Create and return a connection to the MySQL database."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def save_item_report(report_type, date_field):
    """Save a lost-item or found-item report to the database."""
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO items (
                item_name,
                category,
                report_type,
                location,
                report_date,
                description,
                contact_information
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        item_data = (
            request.form["item-name"],
            request.form["category"],
            report_type,
            request.form["location"],
            request.form[date_field],
            request.form["description"],
            request.form["contact"],
        )

        cursor.execute(insert_query, item_data)
        connection.commit()

        return True

    except mysql.connector.Error as error:
        print(f"Item submission failed: {error}")
        return False

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


@app.route("/")
def home():
    """Display the homepage."""
    return render_template("index.html")


@app.route("/report-lost-item", methods=["GET", "POST"])
def report_lost_item():
    """Display the lost-item form and save submitted reports."""
    if request.method == "POST":
        if save_item_report("lost", "date-lost"):
            flash("Lost item report submitted successfully.")
        else:
            flash("Unable to save the lost item report.")

        return redirect(url_for("report_lost_item"))

    return render_template("report-lost-item.html")


@app.route("/report-found-item", methods=["GET", "POST"])
def report_found_item():
    """Display the found-item form and save submitted reports."""
    if request.method == "POST":
        if save_item_report("found", "date-found"):
            flash("Found item report submitted successfully.")
        else:
            flash("Unable to save the found item report.")

        return redirect(url_for("report_found_item"))

    return render_template("report-found-item.html")

@app.route("/items")
def items():
    """Display all reported lost and found items."""
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        select_query = """
            SELECT
                id,
                item_name,
                category,
                report_type,
                location,
                report_date,
                status
            FROM items
            ORDER BY created_at DESC, id DESC
        """

        cursor.execute(select_query)
        item_records = cursor.fetchall()

        return render_template("items.html", items=item_records)

    except mysql.connector.Error as error:
        print(f"Unable to load items: {error}")

        return render_template(
            "items.html",
            items=[],
        ), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

@app.route("/item-details")
def item_details():
    """Redirect users to the item list before selecting an item."""
    return redirect(url_for("items"))


@app.route("/items/<int:item_id>")
def item_detail(item_id):
    """Display the details of one selected item."""
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        select_query = """
            SELECT
                id,
                item_name,
                category,
                report_type,
                location,
                report_date,
                description,
                contact_information,
                status
            FROM items
            WHERE id = %s
        """

        cursor.execute(select_query, (item_id,))
        item = cursor.fetchone()

        if item is None:
            return "Item not found.", 404

        return render_template("item-details.html", item=item)

    except mysql.connector.Error as error:
        print(f"Unable to load item details: {error}")
        return "Unable to load item details.", 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


@app.route("/db-test")
def database_test():
    """Test whether the Flask application can connect to the database."""
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]

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
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()