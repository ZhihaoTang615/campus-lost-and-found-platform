from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return a simple message to confirm that the Flask server is running."""
    return "Campus Lost and Found Platform backend is running."