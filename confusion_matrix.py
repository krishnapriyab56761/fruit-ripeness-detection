import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix
from utils.data_loader import load_datasets

# ----------------------------
# Paths
# ----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "final_dataset"
)

MODEL_DIR = os.path.join(BASE_DIR, "saved_models")

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "results",
    "confusion_matrix"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ----------------------------
# Load Dataset
# ----------------------------

_, _, test_ds, class_names = load_datasets(DATASET)

MODELS = [

    "CustomCNN",
    "MobileNetV2",
    "EfficientNetB0",
    "ResNet50",
    "DenseNet121",
    "Xception"

]

# ----------------------------
# Evaluate Each Model
# ----------------------------

for model_name in MODELS:

    model_path = os.path.join(
        MODEL_DIR,
        f"{model_name}.keras"
    )

    if not os.path.exists(model_path):

        print(f"{model_name} not found.")
        continue

    print(f"\nGenerating confusion matrix for {model_name}")

    model = tf.keras.models.load_model(model_path)

    y_true = []
    y_pred = []

    for images, labels in test_ds:

        predictions = model.predict(images, verbose=0)

        y_true.extend(np.argmax(labels.numpy(), axis=1))
        y_pred.extend(np.argmax(predictions, axis=1))

    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(12,10))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=class_names,
        yticklabels=class_names
    )

    plt.title(f"{model_name} Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.xticks(rotation=90)
    plt.yticks(rotation=0)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            OUTPUT_DIR,
            f"{model_name}.png"
        )
    )

    plt.close()

print("\nAll confusion matrices generated successfully.")