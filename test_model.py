import tensorflow as tf
from utils.data_loader import load_datasets

train_ds, val_ds, test_ds, class_names = load_datasets("../dataset/final_dataset")

print(class_names)