from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Actual results from the four trained models
    results = {
        "Model": [
            "Random Forest",
            "Decision Tree",
            "Logistic Regression",
            "SVM",
        ],
        "Accuracy": [
            0.7728,
            0.7927,
            0.7545,
            0.7532,
        ],
        "Macro F1": [
            0.7719,
            0.7924,
            0.7540,
            0.7527,
        ],
        "Weighted F1": [
            0.7698,
            0.7914,
            0.7526,
            0.7513,
        ],
        "Attack Recall": [
            0.62,
            0.67,
            0.63,
            0.62,
        ],
    }

    df = pd.DataFrame(results)

    # Create results directory
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    # Save comparison table
    csv_path = results_dir / "model_comparison.csv"
    df.to_csv(csv_path, index=False)

    print("\n" + "=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)
    print(df.to_string(index=False))

    print("\n" + "=" * 70)
    print(f"Comparison saved to: {csv_path}")
    print("=" * 70)

    # -----------------------------
    # Accuracy comparison
    # -----------------------------
    plt.figure(figsize=(9, 5))

    plt.bar(df["Model"], df["Accuracy"])

    plt.title("Model Accuracy Comparison")
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.ylim(0, 1)

    plt.xticks(rotation=15)
    plt.tight_layout()

    accuracy_path = results_dir / "accuracy_comparison.png"
    plt.savefig(accuracy_path, dpi=300)
    plt.show()

    # -----------------------------
    # F1-score comparison
    # -----------------------------
    plt.figure(figsize=(9, 5))

    plt.bar(df["Model"], df["Macro F1"])

    plt.title("Model Macro F1-Score Comparison")
    plt.xlabel("Model")
    plt.ylabel("Macro F1-Score")
    plt.ylim(0, 1)

    plt.xticks(rotation=15)
    plt.tight_layout()

    f1_path = results_dir / "f1_comparison.png"
    plt.savefig(f1_path, dpi=300)
    plt.show()

    # -----------------------------
    # Attack Recall comparison
    # -----------------------------
    plt.figure(figsize=(9, 5))

    plt.bar(df["Model"], df["Attack Recall"])

    plt.title("Attack Recall Comparison")
    plt.xlabel("Model")
    plt.ylabel("Attack Recall")
    plt.ylim(0, 1)

    plt.xticks(rotation=15)
    plt.tight_layout()

    recall_path = results_dir / "attack_recall_comparison.png"
    plt.savefig(recall_path, dpi=300)
    plt.show()

    print("\nGenerated graphs:")
    print(accuracy_path)
    print(f1_path)
    print(recall_path)


if __name__ == "__main__":
    main()