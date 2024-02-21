from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class KnotsCrossesCirclePredictor(ImageClassifierPredictor):
    def _get_model(self):
        return BaseModel("knotsCrossesCircle.onnx")

    def is_support(self, variant, instruction):
        return variant == 'knotsCrossesCircle'
