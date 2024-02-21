import base64
import hashlib
import time
from PIL import Image
from flask import Flask, jsonify, request
from io import BytesIO

from funcaptcha_challenger import predict
from util.log import logger
from util.model_support_fetcher import ModelSupportFetcher

app = Flask(__name__)
PORT = 8080
IS_DEBUG = True
fetcher = ModelSupportFetcher()


def process_image(base64_image, variant):
    if base64_image.startswith("data:image/"):
        base64_image = base64_image.split(",")[1]

    image_bytes = base64.b64decode(base64_image)
    image = Image.open(BytesIO(image_bytes))

    ans = predict(image, variant)
    logger.debug(f"predict {variant} result: {ans}")
    return ans


def process_data(data):
    image = data["image"]
    variant = data["variant"]
    ans = {
        "errorId": 0,
        "errorCode": "",
        "status": "ready",
        "solution": {}
    }

    taskId = hashlib.md5(str(int(time.time() * 1000)).encode()).hexdigest()
    ans["taskId"] = taskId
    if variant in fetcher.supported_models:
        ans["solution"]["objects"] = [process_image(image, variant)]
    else:
        ans["errorId"] = 1
        ans["errorCode"] = "ERROR_TYPE_NOT_SUPPORTED"
        ans["status"] = "error"
        ans["solution"]["objects"] = []

    return jsonify(ans)


@app.route("/createTask", methods=["POST"])
def create_task():
    data = request.get_json()
    return process_data(data)


@app.route("/support")
def support():
    return jsonify(fetcher.supported_models)


@app.errorhandler(Exception)
def error_handler(e):
    logger.error(f"error: {e}")
    return jsonify({
        "errorId": 1,
        "errorCode": "ERROR_UNKNOWN",
        "status": "error",
        "solution": {"objects": []}
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=IS_DEBUG, port=PORT)
