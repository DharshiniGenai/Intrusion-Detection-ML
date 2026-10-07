from pathlib import Path

import joblib


def main():
    source_path = Path("models/decision_tree_binary_ids.joblib")
    final_path = Path("models/final_ids_model.joblib")

    print("Loading best model...")
    model = joblib.load(source_path)

    print("Saving final IDS model...")
    joblib.dump(model, final_path)

    print("\n" + "=" * 60)
    print("FINAL MODEL SAVED SUCCESSFULLY")
    print("=" * 60)
    print(f"Source model : {source_path}")
    print(f"Final model  : {final_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()