import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

from src.preprocess import COLUMNS


TRAIN_PATH = "data/KDDTrain+.txt"
TEST_PATH = "data/KDDTest+.txt"
MODEL_PATH = "models/live_ids_model.joblib"


LIVE_NUMERIC_FEATURES = [
    "duration",
    "src_bytes",
    "dst_bytes",
    "src_dst_byte_ratio",
    "byte_rate",
]

LIVE_CATEGORICAL_FEATURES = [
    "protocol_type",
]


def prepare_data(path):
    df = pd.read_csv(path, header=None)
    df.columns = COLUMNS

    df["src_dst_byte_ratio"] = (
        df["src_bytes"] /
        df["dst_bytes"].replace(0, 1)
    )

    df["byte_rate"] = (
        (df["src_bytes"] + df["dst_bytes"]) /
        df["duration"].replace(0, 1)
    )

    features = LIVE_NUMERIC_FEATURES + LIVE_CATEGORICAL_FEATURES

    X = df[features].copy()
    y = (df["attack"] != "normal").astype(int)

    return X, y


print("Loading training data...")
X_train, y_train = prepare_data(TRAIN_PATH)

print("Loading test data...")
X_test, y_test = prepare_data(TEST_PATH)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            LIVE_CATEGORICAL_FEATURES,
        ),
        (
            "numerical",
            StandardScaler(),
            LIVE_NUMERIC_FEATURES,
        ),
    ]
)

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            DecisionTreeClassifier(
                class_weight="balanced",
                random_state=42,
                max_depth=12,
            ),
        ),
    ]
)

print("Training live IDS model...")
model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nLive IDS Model Results")
print("=====================")
print(f"Accuracy: {accuracy:.4f}")
print()
print(
    classification_report(
        y_test,
        predictions,
        target_names=["Normal", "Attack"],
    )
)

joblib.dump(model, MODEL_PATH)

print(f"Model saved to: {MODEL_PATH}")
