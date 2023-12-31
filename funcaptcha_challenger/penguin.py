import numpy as np

from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import FuncaptchaPredictor
from funcaptcha_challenger.tools import check_game_type_3_input_image_size, process_game_type_3_image


class PenguinPredictor(FuncaptchaPredictor):

    def __init__(self):
        super().__init__()
        self.model = BaseModel("penguin.onnx")

    def _check_input_image_size(self, image):
        check_game_type_3_input_image_size(image)

    def _predict(self, image) -> int:
        max_prediction = float('-inf')
        max_index = -1

        for i in range(6):
            ts = process_game_type_3_image(image, i)
            prediction = self._run_prediction(ts)
            prediction_value = prediction[0][0]
            if prediction_value > max_prediction:
                max_prediction = prediction_value
                max_index = i
        return max_index

    def _run_prediction(self, left):
        return self.model.run_prediction(None, {'input': left.astype(np.float32)})[0]
