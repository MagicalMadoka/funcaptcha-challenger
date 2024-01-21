from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class DicematchMatchPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("dicematch.onnx")

    def is_support(self, variant, instruction):
        return 'dicematch' == variant
