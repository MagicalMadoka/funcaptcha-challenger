from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImageClassifierPredictor


class HandNumberPuzzlePredictor(ImageClassifierPredictor):
    def _get_model(self):
        return BaseModel("hand_number_puzzle.onnx")

    def is_support(self, variant, instruction):
        return variant == 'hand_number_puzzle'
