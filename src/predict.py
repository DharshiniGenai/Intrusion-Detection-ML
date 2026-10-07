from pathlib import Path

import joblib
import pandas as pd

from src.preprocess import COLUMNS


PRIMARY_MODEL_PATH = Path("models/final_ids_model.joblib")
ATTACK_MODEL_PATH = Path("models/attack_type_classifier.joblib")


def load_models():
    """Load the primary IDS model and secondary attack-type model."""
    primary_model = joblib.load(PRIMARY_MODEL_PATH)
    attack_model = joblib.load(ATTACK_MODEL_PATH)

    return primary_model, attack_model


def predict_traffic(primary_model, attack_model, traffic_data):
    """
    Predict whether network traffic is Normal or an Attack.

    If the traffic is an Attack, the secondary model
    predicts the attack category.
    """

    if isinstance(traffic_data, dict):
        traffic_data = pd.DataFrame([traffic_data])

    if not isinstance(traffic_data, pd.DataFrame):
        raise TypeError(
            "traffic_data must be a pandas DataFrame or dictionary."
        )

    feature_columns = [
        column
        for column in COLUMNS
        if column not in ["attack", "difficulty"]
    ]

    missing_columns = [
        column
        for column in feature_columns
        if column not in traffic_data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required features: {missing_columns}"
        )

    traffic_data = traffic_data[feature_columns].copy()

    # Primary prediction: Normal or Attack
    primary_prediction = primary_model.predict(traffic_data)[0]

    primary_probabilities = primary_model.predict_proba(traffic_data)[0]
    primary_confidence = float(max(primary_probabilities) * 100)

    if primary_prediction == "Normal":
        return {
            "prediction": "Normal",
            "attack_type": None,
            "confidence": round(primary_confidence, 2),
            "attack_type_confidence": None,
        }

    # Secondary prediction: DoS / Probe / R2L / U2R
    attack_prediction = attack_model.predict(traffic_data)[0]

    attack_probabilities = attack_model.predict_proba(traffic_data)[0]
    attack_confidence = float(max(attack_probabilities) * 100)

    return {
        "prediction": "Attack",
        "attack_type": attack_prediction,
        "confidence": round(primary_confidence, 2),
        "attack_type_confidence": round(attack_confidence, 2),
    }


if __name__ == "__main__":
    print("Loading IDS models...")

    primary_model, attack_model = load_models()

    print("Primary model loaded successfully.")
    print("Attack-type model loaded successfully.")

    print(f"Primary model: {PRIMARY_MODEL_PATH}")
    print(f"Attack-type model: {ATTACK_MODEL_PATH}")