import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load comparison results
df = pd.read_csv("results/comparison/comparison.csv")

models = df["Model"]

precision = df["Precision"]
recall = df["Recall"]
f1 = df["F1-Score"]

x = np.arange(len(models))
width = 0.25

plt.figure(figsize=(10,6))

plt.bar(
    x - width,
    precision,
    width,
    label="Precision"
)

plt.bar(
    x,
    recall,
    width,
    label="Recall"
)

plt.bar(
    x + width,
    f1,
    width,
    label="F1-Score"
)

plt.xticks(x, models, rotation=20)

plt.ylabel("Score (%)")
plt.xlabel("Deep Learning Models")

plt.title("Figure 7.3  Precision, Recall and F1-Score Comparison")

plt.ylim(50,100)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.legend()

plt.tight_layout()

plt.savefig(
    "results/comparison/precision_recall_f1.png",
    dpi=300
)

plt.show()