class FuncaptchaPredictor:
    def __init__(self):
        pass

    def predict(self, image) -> int:
        self._check_input_image_size(image)
        return self._predict(image)

    def _check_input_image_size(self, image):
        pass

    def _predict(self, image) -> int:
        pass
