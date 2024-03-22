from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class UnbentobjectsPredictor(ImageClassifierPredictor):
    def _get_model(self):
        return BaseModel("unbentobjects.onnx")

    def is_support(self, variant, instruction):
        return variant == 'unbentobjects' or instruction == 'Pick the object that is not distorted'
