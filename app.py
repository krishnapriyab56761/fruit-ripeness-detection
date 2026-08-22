import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predict_image

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return "Fruit Ripeness Detection API Running"


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files["image"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(filepath)

    result = predict_image(filepath)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)