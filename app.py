# kroonstad-api/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from data import MOCK_DATA  # Import your mock data

app = Flask(__name__)

# Define the origins that are allowed to access this API
allowed_origins = [
    "http://localhost:5173",  # Local React dev server
    "https://ocp-demo-silke-ai.netlify.app/",  # Your live Netlify domain
]

# Crucial: Configure CORS to only allow the trusted origins above
CORS(app, resources={r"/*": {"origins": allowed_origins}})


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
