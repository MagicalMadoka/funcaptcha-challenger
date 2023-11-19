import hashlib
import json
import os

import requests
from loguru import logger
import onnxruntime as ort
from tqdm import tqdm


class BaseModel:
    version_info = None

    def __init__(self, model_name):
        self.model_name = model_name
        self.ort_session = None

    def _initialize_model(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        model_filename = os.path.join(script_dir, self.model_name)
        version_url = "https://github.com/MagicalMadoka/funcaptcha-challenger/releases/download/model/version.json"
        model_url = f"https://github.com/MagicalMadoka/funcaptcha-challenger/releases/download/model/{self.model_name}"

        if not os.path.exists(model_filename):
            logger.debug(f"model {self.model_name} not found, downloading...")
            self._download_file(model_url, model_filename)
        else:
            logger.debug(f"model {self.model_name} found, checking hash")
            if BaseModel.version_info is None:
                version_json_path = os.path.join(script_dir, "version.json")
                self._download_file(version_url, version_json_path)

                with open(version_json_path, "r") as file:
                    BaseModel.version_info = json.load(file)

            expected_hash = BaseModel.version_info[self.model_name.split(".")[0]]

            if self._file_sha256(model_filename) != expected_hash:
                logger.debug(f"model {model_filename} hash mismatch, downloading...")
                self._download_file(model_url, model_filename)

        self.ort_session = ort.InferenceSession(model_filename)

    def _download_file(self, url, filename):
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
            msg = ('You might be using an outdated version, using pip install --upgrade funcaptcha-challenger might '
                   'solve the issue.')
            logger.error(msg)
            raise Exception(msg)

    def _file_sha256(self, filename):
        sha256_hash = hashlib.sha256()
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def run_prediction(self, output_names, input_feed):
        if self.ort_session is None:
            self._initialize_model()
        return self.ort_session.run(output_names, input_feed)
