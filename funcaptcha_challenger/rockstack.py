from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class RockstackPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("rockstack.onnx")

    def is_support(self, variant, instruction):
        return 'rockstack' == variant
