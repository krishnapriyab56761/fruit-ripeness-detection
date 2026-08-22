"""import tensorflow as tf

model = tf.keras.models.load_model("saved_models/EfficientNetB0.keras")

for layer in model.layers:
    print(layer.name)"""

import tensorflow as tf

model = tf.keras.models.load_model("saved_models/EfficientNetB0.keras")

base = model.get_layer("efficientnetb0")

for layer in base.layers:
    print(layer.name)