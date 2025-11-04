# app.py
import os
from flask import Flask, jsonify
from flask_cors import CORS
from data import MOCK_DATA  # Import your mock data

app = Flask(__name__)

# Define the origins that are allowed to access this API
allowed_origins = [
    "http://localhost:5173",  # Local React dev server
    "https://ocp-demo-silke-ai.netlify.app",  # Your live Netlify domain
]

# Crucial: Configure CORS to only allow the trusted origins above
CORS(app, resources={r"/*": {"origins": allowed_origins}})


@app.route("/api/dashboard", methods=["GET"])
def get_dashboard_data():
    """Returns all mock dashboard data."""
    # This endpoint provides all data needed for the four React views.
    return jsonify(MOCK_DATA)


if __name__ == "__main__":
    # 🌟 CRITICAL: Get HOST and PORT from environment variables 🌟
    # Render sets PORT. We default HOST to 0.0.0.0 and PORT to 5000 for local development.
    HOST = os.environ.get("HOST", "0.0.0.0")
    PORT = int(os.environ.get("PORT", 5000))

    print("--- Operational Certainty Platform API ---")
    print(f"API is serving data at: http://{HOST}:{PORT}/api/dashboard")

    # Pass the environment-set host and port to app.run()
    app.run(host=HOST, port=PORT, debug=True)
