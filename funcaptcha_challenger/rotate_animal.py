import numpy as np

from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.singleton import singleton
from funcaptcha_challenger.tools import check_input_image_size, process_image


class AnimalRotationPredictor:
    def __init__(self):
        self.model = BaseModel("animal_rotation_towards_hand.onnx")


    def _run_prediction(self, left, right):
        return self.model.run_prediction(None, {'input_left': left.astype(np.float32),
                                                'input_right': right.astype(np.float32)})[0]

    def predict(self, image) -> int:
        check_input_image_size(image)

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
