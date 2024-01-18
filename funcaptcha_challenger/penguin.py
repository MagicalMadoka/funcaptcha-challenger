from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class PenguinPredictor(ImageClassifierPredictor):

    def _get_model(self):
        return BaseModel("penguin.onnx")
