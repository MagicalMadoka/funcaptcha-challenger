from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class BrokenJigsawbrokenjigsawSwapPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("BrokenJigsawbrokenjigsaw_swap.onnx")

    def is_support(self, variant, instruction):
        return 'BrokenJigsawbrokenjigsaw_swap' == variant
