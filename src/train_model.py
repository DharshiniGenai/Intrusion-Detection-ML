from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
)
from sklearn.pipeline import Pipeline

from preprocess import (
    DROP_COLUMNS,
    TARGET_COLUMN,
    create_preprocessor,
    load_data,
)


def main():
    print("Loading dataset...")

    train, test = load_data()

    # Separate features and target
    X_train = train.drop(columns=DROP_COLUMNS)
    y_train = train[TARGET_COLUMN]

    X_test = test.drop(columns=DROP_COLUMNS)
    y_test = test[TARGET_COLUMN]

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    # Preprocessing + Random Forest
    model = Pipeline(
        steps=[
            ("preprocessor", create_preprocessor()),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200,
                    random_state=42,
                    n_jobs=-1,
                    class_weight="balanced_subsample",
                ),
            ),
        ]
    )

    print("\nTraining Random Forest...")
    print("Please wait. This may take a few minutes.")

    model.fit(X_train, y_train)

    print("\nTraining completed!")

    # Predictions
    print("\nEvaluating model...")
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average="macro")
    weighted_f1 = f1_score(y_test, y_pred, average="weighted")

    print("\n" + "=" * 60)
    print("MODEL PERFORMANCE")
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

    # Save trained model
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)

    model_path = models_dir / "random_forest_ids.joblib"
    joblib.dump(model, model_path)

    print("\n" + "=" * 60)
    print(f"Model saved to: {model_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()