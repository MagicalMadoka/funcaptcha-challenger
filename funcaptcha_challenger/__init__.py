from funcaptcha_challenger.coordinatesmatch import CoordinatesMatchPredictor
from funcaptcha_challenger.dicematch import DicematchMatchPredictor
from funcaptcha_challenger.hopscotch_highsec import HopscotchHighsecPredictor
from funcaptcha_challenger.numericalmatch import NumericalmatchPredictor
from funcaptcha_challenger.penguin import PenguinPredictor
from funcaptcha_challenger.shadows import ShadowsPredictor
from funcaptcha_challenger.threed_rollball_animal import ThreeDRollballAnimalPredictor
from funcaptcha_challenger.threed_rollball_objects import ThreeDRollballObjectsPredictor
from funcaptcha_challenger.train_coordinates import TrainCoordinatesPredictor

predictors = [
    ThreeDRollballAnimalPredictor(),
    HopscotchHighsecPredictor(),
    ThreeDRollballObjectsPredictor(),
    CoordinatesMatchPredictor(),
    TrainCoordinatesPredictor(),
    DicematchMatchPredictor(),
    PenguinPredictor(),
    ShadowsPredictor(),
]


def predict(image, variant, instruction):
    for predictor in predictors:
        if predictor.is_support(variant, instruction):
            return predictor.predict(image)


predict_numericalmatch = NumericalmatchPredictor().predict

predict_3d_rollball_animals = lambda image: predict(image, '3d_rollball_animals', None)
predict_hopscotch_highsec = lambda image: predict(image, 'hopscotch_highsec', None)
predict_3d_rollball_objects = lambda image: predict(image, '3d_rollball_objects', None)
predict_coordinatesmatch = lambda image: predict(image, 'coordinatesmatch', None)
predict_train_coordinates = lambda image: predict(image, 'train_coordinates', None)
predict_dicematch = lambda image: predict(image, 'dicematch', None)

predict_penguin = lambda image: predict(image, 'penguin', None)
predict_shadows = lambda image: predict(image, 'shadows', None)
