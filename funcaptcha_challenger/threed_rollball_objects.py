import numpy as np

from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.tools import check_input_image_size, process_image, process_ans_image


class ThreeDRollballObjectsPredictor:
    def __init__(self):
        self.model = BaseModel("3d_rollball_objects_v2.onnx")

    def _run_prediction(self, left, right):
        return self.model.run_prediction(None, {'input_left': left.astype(np.float32),
                                                'input_right': right.astype(np.float32)})[0]

    def predict(self, image) -> int:
        check_input_image_size(image)

        max_prediction = float('-inf')
        max_index = -1

        width = image.width
        left = process_ans_image(image)
        for i in range(width // 200):

            right = process_image(image, (0, i))
            prediction = self._run_prediction(left, right)

            prediction_value = prediction[0][0]

            if prediction_value > max_prediction:
                max_prediction = prediction_value
                max_index = i

        return max_index
