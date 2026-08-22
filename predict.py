import numpy as np
import tensorflow as tf
from PIL import Image

# Load model once
model = tf.keras.models.load_model("saved_models/Xception.keras")

CLASS_NAMES = [
    "FreshApple",
    "FreshBanana",
    "FreshGrape",
    "FreshGuava",
    "FreshJujube",
    "FreshOrange",
    "FreshPomegranate",
    "FreshStrawberry",
    "RottenApple",
    "RottenBanana",
    "RottenGrape",
    "RottenGuava",
    "RottenJujube",
    "RottenOrange",
    "RottenPomegranate",
    "RottenStrawberry"
]


def predict_image(image_path):

    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))

    img = np.array(img, dtype=np.float32)
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    idx = np.argmax(prediction)

    confidence = float(np.max(prediction)) * 100

    return {
        "class": CLASS_NAMES[idx],
        "confidence": round(confidence, 2)
    }