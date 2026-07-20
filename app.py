import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename


load_dotenv(dotenv_path=".env", override=True)

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
CLAIM_PENDING_STATUS = "pending"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def get_database_connection():
    """Create and return a connection to the MySQL database."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )


def is_allowed_file(filename):
    """Return True when a filename uses an allowed image extension."""
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def save_claim_request(
    cursor,
    connection,
    item_id,
    claimant_name,
    claimant_contact,
    verification_details,
):
    """Store a new claim request with an initial pending status."""
    insert_query = """
        INSERT INTO claims (
            item_id,
            claimant_name,
            claimant_contact,
            verification_details,
            status
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    claim_data = (
        item_id,
        claimant_name,
        claimant_contact,
        verification_details,
        CLAIM_PENDING_STATUS,
    )

    cursor.execute(insert_query, claim_data)
    connection.commit()


def save_item_report(report_type, date_field):
    """Save a lost-item or found-item report to the database."""
    connection = None
    cursor = None
    image_path = None

    uploaded_file = request.files.get("item-photo")

    if uploaded_file and uploaded_file.filename:
        if not is_allowed_file(uploaded_file.filename):
            flash(
                "Invalid image file type. "
                "Please upload PNG, JPG, JPEG, or GIF."
            )
            return False

        filename = secure_filename(uploaded_file.filename)
        save_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename,
        )

        uploaded_file.save(save_path)
        image_path = f"uploads/{filename}"

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
                contact_information,
                image_path
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        item_data = (
            request.form["item-name"],
            request.form["category"],
            report_type,
            request.form["location"],
            request.form[date_field],
            request.form["description"],
            request.form["contact"],
            image_path,
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
    """Display items and allow users to search and filter results."""
    connection = None
    cursor = None

    search_query = request.args.get("q", "").strip()
    report_type = request.args.get("report_type", "").strip()
    category = request.args.get("category", "").strip()

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
        """

        conditions = []
        parameters = []

        if search_query:
            conditions.append(
                """
                (
                    item_name LIKE %s
                    OR description LIKE %s
                    OR location LIKE %s
                )
                """
            )

            search_pattern = f"%{search_query}%"

            parameters.extend(
                [
                    search_pattern,
                    search_pattern,
                    search_pattern,
                ]
            )

        if report_type:
            conditions.append("report_type = %s")
            parameters.append(report_type)

        if category:
            conditions.append("category = %s")
            parameters.append(category)

        if conditions:
            select_query += " WHERE " + " AND ".join(conditions)

        select_query += " ORDER BY created_at DESC, id DESC"

        cursor.execute(select_query, tuple(parameters))
        item_records = cursor.fetchall()

        return render_template(
            "items.html",
            items=item_records,
            search_query=search_query,
            selected_report_type=report_type,
            selected_category=category,
        )

    except mysql.connector.Error as error:
        print(f"Unable to load items: {error}")

        return render_template(
            "items.html",
            items=[],
            search_query=search_query,
            selected_report_type=report_type,
            selected_category=category,
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
                status,
                image_path
            FROM items
            WHERE id = %s
        """

        cursor.execute(select_query, (item_id,))
        item = cursor.fetchone()

        if item is None:
            return "Item not found.", 404

        return render_template(
            "item-details.html",
            item=item,
        )

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
    """Test whether Flask can connect to the database."""
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
            "message": (
                "Database connection failed. "
                "Check the terminal for details."
            )
        }, 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


@app.route(
    "/claim-request/<int:item_id>",
    methods=["GET", "POST"],
)
def claim_request(item_id):
    """Display and process a claim request for a selected item."""
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM items WHERE id = %s",
            (item_id,),
        )
        item = cursor.fetchone()

        if item is None:
            return "Item not found.", 404

        if request.method == "POST":
            claimant_name = request.form["name"].strip()
            claimant_contact = request.form["contact"].strip()
            verification_details = request.form["message"].strip()

            save_claim_request(
                cursor=cursor,
                connection=connection,
                item_id=item_id,
                claimant_name=claimant_name,
                claimant_contact=claimant_contact,
                verification_details=verification_details,
            )

            flash("Claim submitted successfully!")

            return redirect(
                url_for(
                    "item_detail",
                    item_id=item_id,
                )
            )

        return render_template(
            "claim-request.html",
            item=item,
        )

    except mysql.connector.Error as error:
        print(f"Claim request failed: {error}")
        return "Unable to process the claim request.", 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


print("APP FILE LOADED")


if __name__ == "__main__":
    print("STARTING FLASK SERVER")
    app.run(debug=True)