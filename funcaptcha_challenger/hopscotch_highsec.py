from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class HopscotchHighsecPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("hopscotch_highsec.onnx")

    def is_support(self, variant, instruction):
        return 'hopscotch_highsec' == variant
