from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class FrankenheadPredictor(ImageClassifierPredictor):

    def _get_model(self):
        return BaseModel("frankenhead.onnx")

    def is_support(self, variant, instruction):
        return variant == 'frankenhead'
