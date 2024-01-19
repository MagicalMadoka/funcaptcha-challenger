from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.predictor import ImagePairClassifierPredictor


class TrainCoordinatesPredictor(ImagePairClassifierPredictor):

    def _get_model(self):
        return BaseModel("train_coordinates.onnx")
