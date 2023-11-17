import hashlib
import os
import json
import numpy as np
import onnxruntime as ort
import requests
from loguru import logger

from tqdm import tqdm

class AnimalRotationPredictor:
    def __init__(self, model_name="animal_rotation_towards_hand.onnx"):
        self.model_name = model_name
        self.ort_session = None

    def _initialize_model(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        model_filename = os.path.join(script_dir, self.model_name)
        version_url = "https://github.com/MagicalMadoka/funcaptcha-challenger/releases/download/model/version.json"
        model_url = "https://github.com/MagicalMadoka/funcaptcha-challenger/releases/download/model/animal_rotation_towards_hand.onnx"

        if not os.path.exists(model_filename):
            logger.debug("model file not found, downloading...")
            self._download_file(model_url, model_filename)
        else:
            logger.debug("model file found, checking hash")
            version_json_path = os.path.join(script_dir, "version.json")
            self._download_file(version_url, version_json_path)

            with open(version_json_path, "r") as file:
                version_info = json.load(file)
            expected_hash = version_info["animal_rotation_towards_hand"]

            if self._file_sha256(model_filename) != expected_hash:
                logger.debug("model file hash mismatch, downloading...")
                self._download_file(model_url, model_filename)

        self.ort_session = ort.InferenceSession(model_filename)

    def _process_image(self, image, index, input_shape=(52, 52)):
        x, y = index[1] * 200, index[0] * 200
        sub_image = image.crop((x, y, x + 200, y + 200)).resize(input_shape)
        return np.array(sub_image).transpose(2, 0, 1)[np.newaxis, ...] / 255.0

    def _run_prediction(self, left, right):
        if self.ort_session is None:
            self._initialize_model()
        return self.ort_session.run(None, {'input_left': left.astype(np.float32), 'input_right': right.astype(np.float32)})[0]

    def predict(self, image) -> int:
        if image.height != 400 or image.width % 200 != 0:
            raise ValueError("Image size must be (n * 200) x 400 pixels")

        max_prediction = float('-inf')
        max_index = -1

        width = image.width
        for i in range(width // 200):
            left = self._process_image(image, (0, i))
            right = self._process_image(image, (1, 0))
            prediction = self._run_prediction(left, right)

            prediction_value = prediction[0][0]

            if prediction_value > max_prediction:
                max_prediction = prediction_value
                max_index = i

        return max_index

    def _download_file(self,url, filename):
        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")

    def _file_sha256(self,filename):
        sha256_hash = hashlib.sha256()
        with open(filename,"rb") as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
