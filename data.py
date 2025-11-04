# data.py
# A utility function to generate simple trend data
def generate_trend(start, end, points, dip_day=20, dip_magnitude=-0.05):
    """Generates a list of dictionaries for a simple trend line."""
    data = []
    for i in range(1, points + 1):
        score = start - (i * 0.05)
        if i >= dip_day:
            score += (
                i - dip_day
            ) * dip_magnitude  # Simulate a trend dip for 30-day OHS
        data.append({"day": i, "score": round(score, 2)})
    return data


MOCK_DATA = {
    # --- View 1: Executive Overview (Risk & Financial Impact) ---
    "executive": {
        "ohs_score": 98,
        "ohs_status": "stable",
        # OHS Trend: Stable at 98 for the last 30 days
        "ohs_trend": generate_trend(98.5, 98, 30, dip_day=15, dip_magnitude=0.05),
        "avoided_cost_zar": 5400000,
        "avoided_events": 1,  # Used in the takeaway text
        "critical_asset_risk_matrix": [
            # The focus point: Mill #1 Bearing
            {
                "asset": "Mill #1 Bearing",
                "impact": "High",
                "likelihood": "High",
                "x": 75,
                "y": 75,
            },
            {
                "asset": "Silo Motor #4",
                "impact": "Low",
                "likelihood": "High",
                "x": 75,
                "y": 25,
            },
            {
                "asset": "Conveyor Belt Motor",
                "impact": "High",
                "likelihood": "Low",
                "x": 25,
                "y": 75,
            },
        ],
    },
    # --- View 2: Operations Manager View (Actionable Predictions) ---
    "operations": {
        "alerts_list": [
            {
                "id": 1,
                "asset": "Roller Mill #3 Bearing",
                "fault": "Inner Race Failure",
                "predicted_date": "2026-05-01",
                "confidence": 98,
                "runway_weeks": 6,
                "cmms_wo": "WO-Kroon-1123",
            },
            {
                "id": 2,
                "asset": "Blower Fan #2",
                "fault": "Vane Imbalance",
                "predicted_date": "2026-06-15",
                "confidence": 90,
                "runway_weeks": 12,
            },
        ],
        # RUL Curve Data: Simulated degradation from 100 to 0 over 50 data points
        "rul_curve_data": [
            {"day": i, "health": round(100 - (i * 2.5) + (i / 10), 1)}
            for i in range(41)
        ],  # Line smoothly descends from ~100 to ~0
        "action_threshold": 30,  # The % health where the action threshold is crossed
    },
    # --- View 3: Maintenance Engineer View (Diagnostics and Root Cause) ---
    "engineer_diagnosis": {  # <--- FIXED: Renamed key to match frontend expectation
        # Component Health Drill-Down Metrics
        "component_health_metrics": {
            "RMS Velocity (mm/s)": {"value": 0.85, "standard": 0.5, "status": "Alert"},
            "Crest Factor": {"value": 12.5, "standard": 4.0, "status": "Alert"},
            "Bearing Temp (°C)": {
                "value": 65,
                "standard": 70,
                "status": "Normal",
            },  # Still normal, but trending up
        },
        # Vibration Data (Frequency Domain)
        "vibration_spectrum": [
            {"freq": 10, "amp": 0.5},
            {"freq": 50, "amp": 0.2},
            {"freq": 85, "amp": 4.2},  # BSF Spike (Inner Race Fault Frequency)
            {"freq": 170, "amp": 2.5},  # 2x BSF
            {"freq": 340, "amp": 1.5},  # 4x BSF (Highlight this one)
        ],
        # Temperature Trend showing recent spike
        "temperature_trend": [
            {"hour": i, "temp": 45 + (i * 0.5) if i < 15 else 47 + (i - 15) * 1.5}
            for i in range(24)
        ],
        # Energy Impact Correlation (kW vs. RUL)
        "energy_correlation": [
            {"month": "Oct", "rul": 90, "kw": 15},
            {"month": "Nov", "rul": 70, "kw": 18},
            {"month": "Dec", "rul": 50, "kw": 22},
            {"month": "Jan", "rul": 20, "kw": 28},
        ],
    },
    # --- View 4: PoC Success Metric Tracking (Before & After) ---
    "tracking": {
        "pm_cancellations": 3,
        "labor_saved_days": 3,
        "prediction_accuracy": 98,
    },
}
