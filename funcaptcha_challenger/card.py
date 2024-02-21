from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class CardPredictor(ImageClassifierPredictor):

    def _get_model(self):
        return BaseModel("card.onnx")

    def is_support(self, variant, instruction):
        return variant == 'card'
