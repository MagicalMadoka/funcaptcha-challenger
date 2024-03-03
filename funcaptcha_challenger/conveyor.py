from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class ConveyorPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("conveyor.onnx")

    def is_support(self, variant, instruction):
        return 'conveyor' == variant

    def image_color_mode(self):
        return 'gray'
