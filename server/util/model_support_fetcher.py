import json

import requests
from pipeit import Write, Read

from util.log import logger


class ModelSupportFetcher:
    def __init__(self, model_list_file="model_list.json"):
        self.model_list_file = model_list_file
        self._supported_models = None
        self.fetch_model_list()

    def fetch_model_list(self):
        url = "https://github.com/MagicalMadoka/funcaptcha-challenger/releases/download/model/version.json"
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch model list")
            return None
        data = response.json()
        supported_models = json.dumps(list(data.keys()))
        logger.debug(f"SUPPORTED MODELS: \n{supported_models}")
        Write(self.model_list_file, supported_models)

    @property
    def supported_models(self):
        if self._supported_models is None:
            self._supported_models = Read(self.model_list_file) | json.loads
        return self._supported_models
