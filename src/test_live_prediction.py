import joblib

from src.live_capture import capture_packets
from src.live_features import extract_flow_features
from src.live_preprocess import build_live_features


model = joblib.load("models/live_ids_model.joblib")

packets = capture_packets(
    count=30,
    timeout=15
)

flows = extract_flow_features(packets)

live = build_live_features(flows)

live["protocol_type"] = [
    flow["protocol"]
    for flow in flows
]

features = [
    "duration",
    "src_bytes",
    "dst_bytes",
    "protocol_type",
    "src_dst_byte_ratio",
    "byte_rate",
]

X = live[features]

predictions = model.predict(X)
probabilities = model.predict_proba(X)

print("Flows analyzed:", len(X))

for index, prediction in enumerate(predictions):
    label = "Attack" if prediction == 1 else "Normal"
    confidence = max(probabilities[index]) * 100

    print(
        f"Flow {index + 1}: "
        f"{label} | "
        f"confidence={confidence:.2f}%"
    )
