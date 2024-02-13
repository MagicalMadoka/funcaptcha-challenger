from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class CountingPredictor(ImageClassifierPredictor):

    def _get_model(self):
        return BaseModel("counting.onnx")

    def is_support(self, variant, instruction):
        return variant == 'counting'
