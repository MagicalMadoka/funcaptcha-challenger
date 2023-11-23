import numpy as np

from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import FuncaptchaPredictor
from funcaptcha_challenger.tools import check_input_image_size, process_image


class HopscotchHighsecPredictor(FuncaptchaPredictor):

    def __init__(self):
        super().__init__()
        self.model = BaseModel("hopscotch_highsec.onnx")

    def _check_input_image_size(self, image):
        check_input_image_size(image)

    def _predict(self, image) -> int:

        max_prediction = float('-inf')
        max_index = -1

        width = image.width
        for i in range(width // 200):
            left = process_image(image, (0, i))
            right = process_image(image, (1, 0))
            prediction = self._run_prediction(left, right)

            prediction_value = prediction[0][0]

            if prediction_value > max_prediction:
                max_prediction = prediction_value
                max_index = i

        return max_index

    def _run_prediction(self, left, right):
        return self.model.run_prediction(None, {'input_left': left.astype(np.float32),
                                                'input_right': right.astype(np.float32)})[0]
