from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class PenguinsPredictor(ImageClassifierPredictor):

    def _get_model(self):
        return BaseModel("penguins.onnx")

    def is_support(self, variant, instruction):
        return variant == 'penguins'
