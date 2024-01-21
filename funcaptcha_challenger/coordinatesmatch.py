from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class CoordinatesMatchPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("coordinatesmatch.onnx")

    def is_support(self, variant, instruction):
        return 'coordinatesmatch' == variant
