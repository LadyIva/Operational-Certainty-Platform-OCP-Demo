# kroonstad-api/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from data import MOCK_DATA  # Import your mock data

app = Flask(__name__)
# Crucial: Enable CORS to allow the React frontend (on port 5173) to access this API (on port 5000).
CORS(app)


@app.route("/api/dashboard", methods=["GET"])
def get_dashboard_data():
    """Returns all mock dashboard data."""
    # This endpoint provides all data needed for the four React views.
    return jsonify(MOCK_DATA)


if __name__ == "__main__":
    # Flask runs on port 5000 by default
    print("--- Operational Certainty Platform API ---")
    print("API is serving data at: http://127.0.0.1:5000/api/dashboard")
    app.run(debug=True)
