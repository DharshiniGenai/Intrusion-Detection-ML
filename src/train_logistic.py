from pathlib import Path

import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.pipeline import Pipeline

from preprocess import create_preprocessor, load_data


def main():
    print("Loading dataset...")

    train, test = load_data()

    # Create binary target
    # Normal = Normal traffic
    # Everything else = Attack
    train["binary_target"] = train["category"].apply(
        lambda x: "Normal" if x == "Normal" else "Attack"
    )

    test["binary_target"] = test["category"].apply(
        lambda x: "Normal" if x == "Normal" else "Attack"
    )

    # Features
    X_train = train.drop(
        columns=["attack", "category", "difficulty", "binary_target"]
    )
    y_train = train["binary_target"]

    X_test = test.drop(
        columns=["attack", "category", "difficulty", "binary_target"]
    )
    y_test = test["binary_target"]

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    print("\nBinary class distribution:")
    print(y_train.value_counts())

    # Logistic Regression pipeline
    model = Pipeline(
        steps=[
            ("preprocessor", create_preprocessor()),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    random_state=42,
                ),
            ),
        ]
    )

    print("\nTraining Binary Logistic Regression...")
    print("Please wait. This may take a few minutes.")

    model.fit(X_train, y_train)

    print("\nTraining completed!")

    # Prediction
    print("\nEvaluating model...")
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average="macro")
    weighted_f1 = f1_score(y_test, y_pred, average="weighted")

    print("\n" + "=" * 60)
    print("BINARY LOGISTIC REGRESSION PERFORMANCE")
    print("=" * 60)

    print(f"Accuracy     : {accuracy:.4f}")
    print(f"Macro F1     : {macro_f1:.4f}")
    print(f"Weighted F1  : {weighted_f1:.4f}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            zero_division=0,
        )
    )

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Save model
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)

    model_path = models_dir / "logistic_regression_binary_ids.joblib"
    joblib.dump(model, model_path)

    print("\n" + "=" * 60)
    print(f"Model saved to: {model_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()