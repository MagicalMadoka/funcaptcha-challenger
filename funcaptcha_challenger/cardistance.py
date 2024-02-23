from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class CardistancePredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("cardistance.onnx")

    def is_support(self, variant, instruction):
        return 'cardistance' == variant
