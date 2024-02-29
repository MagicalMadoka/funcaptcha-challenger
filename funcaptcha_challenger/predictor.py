from abc import abstractmethod, ABC

import numpy as np

from funcaptcha_challenger.tools import check_image_pair_classifier_image_size, check_image_classifier_image_size, \
    process_image_classifier_image, process_pair_classifier_ans_image, process_pair_classifier_image


class FuncaptchaPredictor:

    def __init__(self):
        self.model = self._get_model()

    def predict(self, image) -> int:
        self._check_input_image_size(image)
        return self._predict(image)

    @abstractmethod
    def _check_input_image_size(self, image):
        pass

    @abstractmethod
    def _predict(self, image) -> int:
        pass

    @abstractmethod
    def _get_model(self):
        pass

    @abstractmethod
    def is_support(self, variant, instruction):
        pass

    def image_color_mode(self):
        return 'rgb'

    def input_shap(self):
        return (52, 52)


class ImagePairClassifierPredictor(FuncaptchaPredictor, ABC):

    def _check_input_image_size(self, image):
        check_image_pair_classifier_image_size(image)

    def _predict(self, image) -> int:
        max_prediction = float('-inf')
        max_index = -1

        width = image.width
        left = process_pair_classifier_ans_image(image, input_shape=self.input_shap(),
                                                 is_grayscale=self.image_color_mode() == 'gray')
        for i in range(width // 200):

            right = process_pair_classifier_image(image, (0, i), is_grayscale=self.image_color_mode() == 'gray')
            prediction = self._run_prediction(left, right)

            prediction_value = prediction[0][0]

            if prediction_value > max_prediction:
                max_prediction = prediction_value
                max_index = i

        return max_index

    def _run_prediction(self, left, right):
        return self.model.run_prediction(None, {'input_left': left.astype(np.float32),
                                                'input_right': right.astype(np.float32)})[0]


class ImageClassifierPredictor(FuncaptchaPredictor, ABC):

    def _check_input_image_size(self, image):
        check_image_classifier_image_size(image)

    def _predict(self, image) -> int:
        max_prediction = float('-inf')
        max_index = -1

        for i in range(6):
            ts = process_image_classifier_image(image, i, input_shape=self.input_shap(),
                                                is_grayscale=self.image_color_mode() == 'gray')
            prediction = self._run_prediction(ts)
            prediction_value = prediction[0][0]
            if prediction_value > max_prediction:
                max_prediction = prediction_value
                max_index = i
        return max_index

    def _run_prediction(self, image):
        return self.model.run_prediction(None, {'input': image.astype(np.float32)})[0]
