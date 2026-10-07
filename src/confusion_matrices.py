from pathlib import Path

import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from preprocess import load_data


def main():
    print("Loading test dataset...")

    _, test = load_data()

    # Create binary target
    test["binary_target"] = test["category"].apply(
        lambda x: "Normal" if x == "Normal" else "Attack"
    )

    # Test features and target
    X_test = test.drop(
        columns=["attack", "category", "difficulty", "binary_target"]
    )
    y_test = test["binary_target"]

    models = {
        "Random Forest": "models/random_forest_binary_ids.joblib",
        "Decision Tree": "models/decision_tree_binary_ids.joblib",
        "Logistic Regression": "models/logistic_regression_binary_ids.joblib",
        "SVM": "models/svm_binary_ids.joblib",
    }

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    labels = ["Attack", "Normal"]

    for model_name, model_path in models.items():

        print(f"\nEvaluating {model_name}...")

        model = joblib.load(model_path)

        y_pred = model.predict(X_test)

        cm = confusion_matrix(
            y_test,
            y_pred,
            labels=labels,
        )

        print("Confusion Matrix:")
        print(cm)

        display = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=labels,
        )

        display.plot()

        plt.title(f"{model_name} - Confusion Matrix")
        plt.tight_layout()

        filename = (
            model_name.lower()
            .replace(" ", "_")
            + "_confusion_matrix.png"
        )

        output_path = results_dir / filename

        plt.savefig(output_path, dpi=300)
        plt.show()
        plt.close()

        print(f"Saved to: {output_path}")

    print("\n" + "=" * 60)
    print("CONFUSION MATRICES GENERATED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()