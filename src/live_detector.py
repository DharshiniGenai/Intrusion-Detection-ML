import joblib

from src.live_capture import capture_packets
from src.live_features import extract_flow_features
from src.live_preprocess import build_live_features


MODEL_PATH = "models/live_ids_model.joblib"

LIVE_MODEL_FEATURES = [
    "duration",
    "src_bytes",
    "dst_bytes",
    "protocol_type",
    "src_dst_byte_ratio",
    "byte_rate",
]


def load_live_model():
    """Load the trained live IDS model."""
    return joblib.load(MODEL_PATH)


def analyze_live_traffic(count=30, timeout=15):
    """
    Capture live network traffic and classify each extracted flow.

    Returns:
        List of dictionaries containing flow information,
        prediction, and confidence.
    """
    model = load_live_model()

    packets = capture_packets(
        count=count,
        timeout=timeout,
    )

    flows = extract_flow_features(packets)

    if not flows:
        return []

    live_features = build_live_features(flows)

    live_features["protocol_type"] = [
        flow["protocol"]
        for flow in flows
    ]

    X = live_features[LIVE_MODEL_FEATURES]

    predictions = model.predict(X)
    probabilities = model.predict_proba(X)

    results = []

    for index, prediction in enumerate(predictions):
        confidence = float(
            max(probabilities[index]) * 100
        )

        results.append(
            {
                "src_ip": flows[index]["src_ip"],
                "dst_ip": flows[index]["dst_ip"],
                "src_port": flows[index]["src_port"],
                "dst_port": flows[index]["dst_port"],
                "protocol": flows[index]["protocol"],
                "duration": flows[index]["duration"],
                "packet_count": flows[index]["packet_count"],
                "src_bytes": flows[index]["src_bytes"],
                "dst_bytes": flows[index]["dst_bytes"],
                "prediction": (
                    "Attack"
                    if prediction == 1
                    else "Normal"
                ),
                "confidence": round(confidence, 2),
            }
        )

    return results


if __name__ == "__main__":
    results = analyze_live_traffic()

    print(f"Flows analyzed: {len(results)}")

    for index, result in enumerate(results, start=1):
        print(
            f"Flow {index}: "
            f"{result['prediction']} | "
            f"confidence={result['confidence']:.2f}% | "
            f"{result['src_ip']}:{result['src_port']} "
            f"-> "
            f"{result['dst_ip']}:{result['dst_port']} "
            f"({result['protocol']})"
        )
