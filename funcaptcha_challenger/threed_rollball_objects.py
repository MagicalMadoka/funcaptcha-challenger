from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class ThreeDRollballObjectsPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("3d_rollball_objects_v2.onnx")

    def is_support(self, variant, instruction):
        return '3d_rollball_objects' == variant
