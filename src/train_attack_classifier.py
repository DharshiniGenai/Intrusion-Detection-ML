import joblib

from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

from preprocess import load_data, create_preprocessor, DROP_COLUMNS


MODEL_PATH = "models/attack_type_classifier.joblib"


def main():
    print("Loading NSL-KDD data...")

    train, test = load_data()

    # Keep only attack records for secondary classification.
    train = train[train["category"] != "Normal"].copy()
    test = test[test["category"] != "Normal"].copy()

    feature_columns = [
        column
        for column in train.columns
        if column not in ["attack", "category", "difficulty"]
    ]

    X_train = train[feature_columns]
    y_train = train["category"]

    X_test = test[feature_columns]
    y_test = test["category"]

    print("\nAttack categories:")
    print(y_train.value_counts())

    preprocessor = create_preprocessor()

    model = DecisionTreeClassifier(
        random_state=42,
        class_weight="balanced",
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", model),
        ]
    )

    print("\nTraining attack-type classifier...")

    pipeline.fit(X_train, y_train)

    print("Training completed.")

    print("\nEvaluating attack-type classifier...")

    predictions = pipeline.predict(X_test)

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=["DoS", "Probe", "R2L", "U2R"],
            zero_division=0,
        )
    )

    print("Confusion Matrix:")
    print(
        confusion_matrix(
            y_test,
            predictions,
            labels=["DoS", "Probe", "R2L", "U2R"],
        )
    )

    joblib.dump(pipeline, MODEL_PATH)

    print(f"\nAttack-type model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()