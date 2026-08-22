"""import os
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    matthews_corrcoef,
    roc_auc_score
)

from utils.data_loader import load_datasets

# =====================================================
# Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "final_dataset"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "saved_models"
)

RESULT_DIR = os.path.join(
    BASE_DIR,
    "results",
    "comparison"
)

os.makedirs(RESULT_DIR, exist_ok=True)

# =====================================================
# Load Dataset
# =====================================================

print("Loading Dataset...")

train_ds, val_ds, test_ds, class_names = load_datasets(DATASET)

NUM_CLASSES = len(class_names)

print("Classes:")
print(class_names)

# =====================================================
# Models
# =====================================================

MODELS = [

    "CustomCNN",

    "MobileNetV2",

    "EfficientNetB0",

    "ResNet50",

    "DenseNet121",

    "Xception"

]

results = []

# =====================================================
# Evaluation
# =====================================================

for model_name in MODELS:

    print("\n" + "=" * 60)
    print(f"Evaluating {model_name}")
    print("=" * 60)

    model_path = os.path.join(
        MODEL_DIR,
        f"{model_name}.keras"
    )

    if not os.path.exists(model_path):

        print(f"{model_name} model not found.")
        continue

    model = tf.keras.models.load_model(model_path)

    # ------------------------
    # Evaluate Loss & Accuracy
    # ------------------------

    loss, accuracy = model.evaluate(
        test_ds,
        verbose=0
    )

    y_true = []
    y_pred = []
    y_prob = []

    # ------------------------
    # Predictions
    # ------------------------

    for images, labels in test_ds:

        predictions = model.predict(
            images,
            verbose=0
        )

        y_prob.extend(predictions)

        y_true.extend(
            np.argmax(labels.numpy(), axis=1)
        )

        y_pred.extend(
            np.argmax(predictions, axis=1)
        )

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_prob = np.array(y_prob)

    # ------------------------
    # Precision
    # ------------------------

    precision = precision_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    # ------------------------
    # Recall
    # ------------------------

    recall = recall_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    # ------------------------
    # F1 Score
    # ------------------------

    f1 = f1_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

   

    # ------------------------
    # ROC-AUC
    # ------------------------

    y_true_onehot = tf.keras.utils.to_categorical(
        y_true,
        num_classes=NUM_CLASSES
    )

    roc_auc = roc_auc_score(
        y_true_onehot,
        y_prob,
        average="weighted",
        multi_class="ovr"
    )

    # ------------------------
    # Save Result
    # ------------------------

    results.append({

        "Model": model_name,

        "Accuracy": round(accuracy * 100, 2),

        "Loss": round(loss, 4),

        "Precision": round(precision * 100, 2),

        "Recall": round(recall * 100, 2),

        "F1-Score": round(f1 * 100, 2),

       

        "ROC-AUC": round(roc_auc * 100, 2)

    })

# =====================================================
# Save Results
# =====================================================

df = pd.DataFrame(results)

df = df.sort_values(
    by="Accuracy",
    ascending=False
)

csv_path = os.path.join(
    RESULT_DIR,
    "comparison.csv"
)

df.to_csv(
    csv_path,
    index=False
)"""
import os
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    matthews_corrcoef,
    roc_auc_score
)

from utils.data_loader import load_datasets

# =====================================================
# Paths
# =====================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "final_dataset"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "saved_models"
)

RESULT_DIR = os.path.join(
    BASE_DIR,
    "results",
    "comparison"
)

os.makedirs(RESULT_DIR, exist_ok=True)

# =====================================================
# Load Dataset
# =====================================================

print("Loading Dataset...")

train_ds, val_ds, test_ds, class_names = load_datasets(DATASET)

NUM_CLASSES = len(class_names)

print("Classes:")
print(class_names)

# =====================================================
# Models
# =====================================================

MODELS = [

    "CustomCNN",

    "MobileNetV2",

    "EfficientNetB0",

    "ResNet50",

    "DenseNet121",

    "Xception"

]

results = []

# =====================================================
# Evaluation
# =====================================================

for model_name in MODELS:

    print("\n" + "=" * 60)
    print(f"Evaluating {model_name}")
    print("=" * 60)

    model_path = os.path.join(
        MODEL_DIR,
        f"{model_name}.keras"
    )

    if not os.path.exists(model_path):

        print(f"{model_name} model not found.")
        continue

    model = tf.keras.models.load_model(model_path)

    # ------------------------
    # Evaluate Loss & Accuracy
    # ------------------------

    loss, accuracy = model.evaluate(
        test_ds,
        verbose=0
    )

    y_true = []
    y_pred = []
    y_prob = []

    # ------------------------
    # Predictions
    # ------------------------

    for images, labels in test_ds:

        predictions = model.predict(
            images,
            verbose=0
        )

        y_prob.extend(predictions)

        y_true.extend(
            np.argmax(labels.numpy(), axis=1)
        )

        y_pred.extend(
            np.argmax(predictions, axis=1)
        )

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_prob = np.array(y_prob)

    # ------------------------
    # Precision
    # ------------------------

    precision = precision_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    # ------------------------
    # Recall
    # ------------------------

    recall = recall_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    # ------------------------
    # F1 Score
    # ------------------------

    f1 = f1_score(
        y_true,
        y_pred,
        average="weighted",
        zero_division=0
    )

    # ------------------------
    # Specificity
    # ------------------------

    cm = confusion_matrix(y_true, y_pred)

    specificity_list = []

    for i in range(NUM_CLASSES):

        TP = cm[i, i]

        FN = np.sum(cm[i, :]) - TP

        FP = np.sum(cm[:, i]) - TP

        TN = np.sum(cm) - (TP + FP + FN)

        if (TN + FP) == 0:
            specificity = 0
        else:
            specificity = TN / (TN + FP)

        specificity_list.append(specificity)

    specificity = np.mean(specificity_list)

    # ------------------------
    # MCC
    # ------------------------

    mcc = matthews_corrcoef(
        y_true,
        y_pred
    )

    # ------------------------
    # ROC-AUC
    # ------------------------

    y_true_onehot = tf.keras.utils.to_categorical(
        y_true,
        num_classes=NUM_CLASSES
    )

    roc_auc = roc_auc_score(
        y_true_onehot,
        y_prob,
        average="weighted",
        multi_class="ovr"
    )

    # ------------------------
    # Save Result
    # ------------------------

    results.append({

        "Model": model_name,

        "Accuracy": round(accuracy * 100, 2),

        "Loss": round(loss, 4),

        "Precision": round(precision * 100, 2),

        "Recall": round(recall * 100, 2),

        "F1-Score": round(f1 * 100, 2),

        "Specificity": round(specificity * 100, 2),

        "MCC": round(mcc, 4),

        "ROC-AUC": round(roc_auc * 100, 2)

    })

# =====================================================
# Save Results
# =====================================================

df = pd.DataFrame(results)

df = df.sort_values(
    by="Accuracy",
    ascending=False
)

csv_path = os.path.join(
    RESULT_DIR,
    "comparison.csv"
)

df.to_csv(
    csv_path,
    index=False
)

print("\nComparison saved successfully.")
print(df)

print("\nCSV Saved at:")
print(csv_path)
print("\nComparison saved successfully.")
print(df)

print("\nCSV Saved at:")
print(csv_path)