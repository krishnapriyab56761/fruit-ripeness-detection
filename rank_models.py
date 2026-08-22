import os
import pandas as pd

# ----------------------------
# Paths
# ----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_PATH = os.path.join(
    BASE_DIR,
    "results",
    "comparison",
    "comparison.csv"
)

OUTPUT_PATH = os.path.join(
    BASE_DIR,
    "results",
    "comparison",
    "model_ranking.csv"
)

# ----------------------------
# Load comparison.csv
# ----------------------------

df = pd.read_csv(CSV_PATH)

# ----------------------------
# Rank Models
# ----------------------------

ranking = df.sort_values(
    by="Accuracy",
    ascending=False
).reset_index(drop=True)

ranking.insert(0, "Rank", range(1, len(ranking) + 1))

ranking.to_csv(OUTPUT_PATH, index=False)

# ----------------------------
# Display Ranking
# ----------------------------

print("\n" + "=" * 60)
print("MODEL RANKING")
print("=" * 60)

print(ranking)

best = ranking.iloc[0]

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print(f"Model      : {best['Model']}")
print(f"Accuracy   : {best['Accuracy']:.2f}%")
print(f"Loss       : {best['Loss']:.4f}")
print(f"Precision  : {best['Precision']:.2f}%")
print(f"Recall     : {best['Recall']:.2f}%")
print(f"F1-Score   : {best['F1-Score']:.2f}%")

print("\nRanking saved successfully!")
print(f"Saved to: {OUTPUT_PATH}")