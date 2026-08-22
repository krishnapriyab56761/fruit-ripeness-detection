import os
import numpy as np
import tensorflow as tf

from sklearn.metrics import classification_report
from utils.data_loader import load_datasets

# ---------------------------------
# Paths
# ---------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "final_dataset"
)

MODEL_DIR = os.path.join(BASE_DIR, "saved_models")

REPORT_DIR = os.path.join(
    BASE_DIR,
    "results",
    "reports"
)

os.makedirs(REPORT_DIR, exist_ok=True)

REPORT_FILE = os.path.join(
    REPORT_DIR,
    "classification_report.txt"
)

# ---------------------------------
# Load Dataset
# ---------------------------------

_, _, test_ds, class_names = load_datasets(DATASET)

MODELS = [

    "CustomCNN",

    "MobileNetV2",

    "EfficientNetB0",

    "ResNet50",

    "DenseNet121",

    "Xception"

]

# ---------------------------------
# Generate Reports
# ---------------------------------

with open(REPORT_FILE, "w", encoding="utf-8") as f:

    for model_name in MODELS:

        model_path = os.path.join(
            MODEL_DIR,
            f"{model_name}.keras"
        )

        if not os.path.exists(model_path):

            print(f"{model_name} not found.")
            continue

        print(f"Generating report for {model_name}")

        model = tf.keras.models.load_model(model_path)

        y_true = []
        y_pred = []

        for images, labels in test_ds:

            predictions = model.predict(
                images,
                verbose=0
            )

            y_true.extend(
                np.argmax(labels.numpy(), axis=1)
            )

            y_pred.extend(
                np.argmax(predictions, axis=1)
            )

        report = classification_report(

            y_true,

            y_pred,

            target_names=class_names,

            digits=4,

            zero_division=0

        )

        f.write("=" * 80 + "\n")
        f.write(f"{model_name}\n")
        f.write("=" * 80 + "\n\n")
        f.write(report)
        f.write("\n\n")

print("\nClassification report generated successfully.")
print(f"Saved to: {REPORT_FILE}")