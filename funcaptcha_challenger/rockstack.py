from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class RockstackPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("rockstack_v2.onnx")

    def is_support(self, variant, instruction):
        return 'rockstack' == variant

    def image_color_mode(self):
        return 'gray'
