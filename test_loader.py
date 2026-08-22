import os
from utils.data_loader import load_datasets

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(
    BASE_DIR,
    "..",
    "dataset",
    "final_dataset"
)

train_ds, val_ds, test_ds, class_names = load_datasets(DATASET)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print(f"Training Batches   : {len(train_ds)}")
print(f"Validation Batches : {len(val_ds)}")
print(f"Testing Batches    : {len(test_ds)}")

print("\nClasses Found:")

for i, cls in enumerate(class_names, start=1):
    print(f"{i}. {cls}")

print(f"\nTotal Classes: {len(class_names)}")