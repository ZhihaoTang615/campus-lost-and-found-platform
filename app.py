import os
import re
from functools import wraps
from urllib.parse import unquote, urlsplit

import mysql.connector
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"), override=False)

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
CLAIM_PENDING_STATUS = "pending"
USER_ROLE = "user"
ADMIN_ROLE = "admin"
MINIMUM_PASSWORD_LENGTH = 8
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
PUBLIC_STATIC_ASSETS = frozenset(
    {
        "css/style.css",
        "js/ui-feedback.js",
    }
)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def is_safe_next_url(target):
    """Return True only for local absolute-path redirect destinations."""
    decoded_target = unquote(target) if target else ""

    if (
        not target
        or not target.startswith("/")
        or target.startswith("//")
        or not decoded_target.startswith("/")
        or decoded_target.startswith("//")
        or "\\" in decoded_target
        or any(ord(character) < 32 for character in decoded_target)
    ):
        return False

    parsed_target = urlsplit(target)

    return not parsed_target.scheme and not parsed_target.netloc


def login_redirect():
    """Redirect an unauthenticated visitor to login with a safe return path."""
    next_url = request.full_path.rstrip("?")

    if is_safe_next_url(next_url):
        return redirect(url_for("login", next=next_url))

    return redirect(url_for("login"))


def get_authenticated_user_id():
    """Return a positive integer session user ID, or None when invalid."""
    user_id = session.get("user_id")

    if isinstance(user_id, bool) or not isinstance(user_id, int):
        return None

    return user_id if user_id > 0 else None


@app.context_processor
def inject_authentication_state():
    """Expose the same validated authentication state used by decorators."""
    return {"is_authenticated": get_authenticated_user_id() is not None}


def login_required(view_function):
    """Require a signed-in account before calling a route function."""

    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if get_authenticated_user_id() is None:
            flash("Please log in to continue.")
            return login_redirect()

        return view_function(*args, **kwargs)

    return wrapped_view


def admin_required(view_function):
    """Require an administrator role stored in the signed Flask session."""

    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if get_authenticated_user_id() is None:
            flash("Please log in to continue.")
            return login_redirect()

        if session.get("user_role") != ADMIN_ROLE:
            return "Administrator access required.", 403

        return view_function(*args, **kwargs)

    return wrapped_view


def is_valid_email(email):
    """Apply basic length and format validation to a normalized email."""
    return len(email) <= 150 and EMAIL_PATTERN.fullmatch(email) is not None


def authenticated_destination():
    """Return the appropriate landing page for the current session role."""
    if session.get("user_role") == ADMIN_ROLE:
        return url_for("admin_dashboard")

    return url_for("my_reports")


def close_database_resources(cursor, connection):
    """Close optional MySQL resources using the application's conventions."""
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()


@app.before_request
def require_secret_key():
    """Refuse requests when no environment-provided session secret exists."""
    if not app.config.get("SECRET_KEY"):
        raise RuntimeError(
            "APP_SECRET_KEY must be configured before starting the application."
        )


@app.before_request
def protect_non_public_static_assets():
    """Expose logged-out visitors only to assets used by public entry pages."""
    if request.endpoint != "static" or get_authenticated_user_id() is not None:
        return None

    static_filename = (request.view_args or {}).get("filename", "")

    if static_filename not in PUBLIC_STATIC_ASSETS:
        flash("Please log in to continue.")
        return login_redirect()

    return None


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
    user_id = get_authenticated_user_id()

    if user_id is None:
        return False

    insert_query = """
        INSERT INTO claims (
            item_id,
            claimant_name,
            claimant_contact,
            verification_details,
            status,
            user_id
        )
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    claim_data = (
        item_id,
        claimant_name,
        claimant_contact,
        verification_details,
        CLAIM_PENDING_STATUS,
        user_id,
    )

    cursor.execute(insert_query, claim_data)
    connection.commit()
    return True


def save_item_report(report_type, date_field):
    """Save a lost-item or found-item report to the database."""
    connection = None
    cursor = None
    image_path = None
    user_id = get_authenticated_user_id()

    if user_id is None:
        return False

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
                image_path,
                user_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
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
            user_id,
        )

        cursor.execute(insert_query, item_data)
        connection.commit()

        return True

    except mysql.connector.Error as error:
        print(f"Item submission failed: {error}")
        return False

    finally:
        close_database_resources(cursor, connection)


@app.route("/")
def home():
    """Display the homepage."""
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Create a public user account with a securely hashed password."""
    if get_authenticated_user_id() is not None:
        return redirect(authenticated_destination())

    full_name = ""
    email = ""

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if (
            not full_name
            or not email
            or not password
            or not confirm_password
            or not password.strip()
            or not confirm_password.strip()
        ):
            flash("All registration fields are required.")
        elif len(full_name) > 100:
            flash("Full name must be 100 characters or fewer.")
        elif not is_valid_email(email):
            flash("Please enter a valid email address.")
        elif len(password) < MINIMUM_PASSWORD_LENGTH:
            flash("Password must be at least 8 characters long.")
        elif password != confirm_password:
            flash("Password and confirmation do not match.")
        else:
            connection = None
            cursor = None

            try:
                connection = get_database_connection()
                cursor = connection.cursor(dictionary=True)
                cursor.execute(
                    "SELECT id FROM users WHERE email = %s",
                    (email,),
                )

                if cursor.fetchone() is not None:
                    flash("An account with that email already exists.")
                else:
                    password_hash = generate_password_hash(password)

                    cursor.execute(
                        """
                        INSERT INTO users (
                            full_name,
                            email,
                            password_hash,
                            role
                        )
                        VALUES (%s, %s, %s, %s)
                        """,
                        (full_name, email, password_hash, USER_ROLE),
                    )
                    connection.commit()

                    flash("Registration successful. Please log in.")
                    return redirect(url_for("login"))

            except mysql.connector.IntegrityError:
                flash("An account with that email already exists.")
            except mysql.connector.Error as error:
                app.logger.error("Registration database error: %s", error)
                flash("Unable to create the account at this time.")
                return render_template(
                    "register.html",
                    full_name=full_name,
                    email=email,
                ), 500
            finally:
                close_database_resources(cursor, connection)

    return render_template(
        "register.html",
        full_name=full_name,
        email=email,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Authenticate a user without disclosing whether an email exists."""
    if request.method == "GET" and get_authenticated_user_id() is not None:
        return redirect(authenticated_destination())

    email = ""
    requested_next = request.values.get("next", "").strip()
    safe_next = requested_next if is_safe_next_url(requested_next) else ""

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        connection = None
        cursor = None

        try:
            user = None

            if email and password and is_valid_email(email):
                connection = get_database_connection()
                cursor = connection.cursor(dictionary=True)
                cursor.execute(
                    """
                    SELECT id, full_name, password_hash, role
                    FROM users
                    WHERE email = %s
                    """,
                    (email,),
                )
                user = cursor.fetchone()

            password_is_valid = False

            if user is not None:
                try:
                    password_is_valid = check_password_hash(
                        user["password_hash"],
                        password,
                    )
                except (TypeError, ValueError):
                    password_is_valid = False

            if user is None or not password_is_valid:
                flash("Invalid email or password.")
            else:
                role = (
                    ADMIN_ROLE
                    if user.get("role") == ADMIN_ROLE
                    else USER_ROLE
                )

                session.clear()
                session["user_id"] = user["id"]
                session["user_name"] = user["full_name"]
                session["user_role"] = role

                destination = authenticated_destination()

                if safe_next:
                    next_path = urlsplit(safe_next).path
                    targets_admin = (
                        next_path == "/admin"
                        or next_path.startswith("/admin/")
                        or next_path == "/db-test"
                    )

                    if role == ADMIN_ROLE or not targets_admin:
                        destination = safe_next

                flash("Login successful.")
                return redirect(destination)

        except mysql.connector.Error as error:
            app.logger.error("Login database error: %s", error)
            flash("Unable to log in at this time.")
            return render_template(
                "login.html",
                email=email,
                next_url=safe_next,
            ), 500
        finally:
            close_database_resources(cursor, connection)

    return render_template(
        "login.html",
        email=email,
        next_url=safe_next,
    )


@app.post("/logout")
@login_required
def logout():
    """Clear all session state and return to the public homepage."""
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.get("/my-reports")
@login_required
def my_reports():
    """Display only item reports owned by the authenticated account."""
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT
                id,
                item_name,
                report_type,
                category,
                location,
                report_date,
                status
            FROM items
            WHERE user_id = %s
            ORDER BY created_at DESC, id DESC
            """,
            (session["user_id"],),
        )
        item_records = cursor.fetchall()

        return render_template(
            "my-reports.html",
            items=item_records,
        )

    except mysql.connector.Error as error:
        app.logger.error("Unable to load My Reports: %s", error)
        return render_template("my-reports.html", items=[]), 500
    finally:
        close_database_resources(cursor, connection)


@app.get("/admin")
@admin_required
def admin_dashboard():
    """Display a read-only overview of every item and claim record."""
    connection = None
    cursor = None
    summary = {
        "total_items": 0,
        "total_lost_reports": 0,
        "total_found_reports": 0,
        "total_claims": 0,
        "pending_claims": 0,
    }

    try:
        connection = get_database_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT
                (SELECT COUNT(*) FROM items) AS total_items,
                (
                    SELECT COUNT(*)
                    FROM items
                    WHERE report_type = %s
                ) AS total_lost_reports,
                (
                    SELECT COUNT(*)
                    FROM items
                    WHERE report_type = %s
                ) AS total_found_reports,
                (SELECT COUNT(*) FROM claims) AS total_claims,
                (
                    SELECT COUNT(*)
                    FROM claims
                    WHERE status = %s
                ) AS pending_claims
            """,
            ("lost", "found", CLAIM_PENDING_STATUS),
        )
        summary_record = cursor.fetchone()

        if summary_record:
            summary.update(summary_record)

        cursor.execute(
            """
            SELECT
                i.id,
                i.item_name,
                i.report_type,
                i.category,
                i.location,
                i.report_date,
                i.status,
                u.full_name AS reporter_name
            FROM items AS i
            LEFT JOIN users AS u ON i.user_id = u.id
            ORDER BY i.created_at DESC, i.id DESC
            """
        )
        item_records = cursor.fetchall()

        cursor.execute(
            """
            SELECT
                c.id,
                i.item_name,
                c.claimant_name,
                c.claimant_contact,
                c.verification_details,
                c.status,
                u.full_name AS registered_account_name,
                c.created_at
            FROM claims AS c
            LEFT JOIN items AS i ON c.item_id = i.id
            LEFT JOIN users AS u ON c.user_id = u.id
            ORDER BY c.created_at DESC, c.id DESC
            """
        )
        claim_records = cursor.fetchall()

        return render_template(
            "admin-dashboard.html",
            summary=summary,
            items=item_records,
            claims=claim_records,
        )

    except mysql.connector.Error as error:
        app.logger.error("Unable to load admin dashboard: %s", error)
        return render_template(
            "admin-dashboard.html",
            summary=summary,
            items=[],
            claims=[],
        ), 500
    finally:
        close_database_resources(cursor, connection)


@app.route("/report-lost-item", methods=["GET", "POST"])
@login_required
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
@login_required
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
@login_required
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
        close_database_resources(cursor, connection)


@app.route("/item-details")
@login_required
def item_details():
    """Redirect users to the item list before selecting an item."""
    return redirect(url_for("items"))


@app.route("/items/<int:item_id>")
@login_required
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
        close_database_resources(cursor, connection)


@app.route("/db-test")
@admin_required
def database_test():
    """Allow an administrator to test the configured database connection."""
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
        close_database_resources(cursor, connection)


@app.route("/claim-success/<int:item_id>")
@login_required
def claim_success(item_id):
    """Display confirmation after a claim request is stored."""
    return render_template(
        "claim-success.html",
        item_id=item_id,
        claim_status=CLAIM_PENDING_STATUS,
    )


@app.route(
    "/claim-request/<int:item_id>",
    methods=["GET", "POST"],
)
@login_required
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

            if (
                not claimant_name
                or not claimant_contact
                or not verification_details
            ):
                flash("All claim fields are required.")
                return render_template(
                    "claim-request.html",
                    item=item,
                ), 200

            claim_was_saved = save_claim_request(
                cursor=cursor,
                connection=connection,
                item_id=item_id,
                claimant_name=claimant_name,
                claimant_contact=claimant_contact,
                verification_details=verification_details,
            )

            if not claim_was_saved:
                flash("Please log in to continue.")
                return login_redirect()

            return redirect(
                url_for(
                    "claim_success",
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
        close_database_resources(cursor, connection)


print("APP FILE LOADED")


if __name__ == "__main__":
    require_secret_key()
    print("STARTING FLASK SERVER")
    app.run()
