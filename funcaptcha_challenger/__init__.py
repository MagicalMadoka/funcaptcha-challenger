import io

from PIL import Image

from funcaptcha_challenger.BrokenJigsawbrokenjigsaw_swap import BrokenJigsawbrokenjigsawSwapPredictor
from funcaptcha_challenger.card import CardPredictor
from funcaptcha_challenger.cardistance import CardistancePredictor
from funcaptcha_challenger.conveyor import ConveyorPredictor
from funcaptcha_challenger.coordinatesmatch import CoordinatesMatchPredictor
from funcaptcha_challenger.counting import CountingPredictor
from funcaptcha_challenger.dicematch import DicematchMatchPredictor
from funcaptcha_challenger.frankenhead import FrankenheadPredictor
from funcaptcha_challenger.hand_number_puzzle import HandNumberPuzzlePredictor
from funcaptcha_challenger.hopscotch_highsec import HopscotchHighsecPredictor
from funcaptcha_challenger.knotsCrossesCircle import KnotsCrossesCirclePredictor
from funcaptcha_challenger.numericalmatch import NumericalmatchPredictor
from funcaptcha_challenger.penguins import PenguinsPredictor
from funcaptcha_challenger.penguins_icon import PenguinsIconPredictor
from funcaptcha_challenger.rockstack import RockstackPredictor
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
    RockstackPredictor(),
    PenguinsPredictor(),
    ShadowsPredictor(),
    FrankenheadPredictor(),
    BrokenJigsawbrokenjigsawSwapPredictor(),
    CountingPredictor(),
    HandNumberPuzzlePredictor(),
    KnotsCrossesCirclePredictor(),
    CardPredictor(),
    CardistancePredictor(),
    PenguinsIconPredictor(),
    ConveyorPredictor()
]


def predict(image, variant, instruction=None):
    for predictor in predictors:
        if predictor.is_support(variant, instruction):
            return predictor.predict(image)


def predict_from_bytes(image_bytes, variant, instruction):
    image_stream = io.BytesIO(image_bytes)
    image = Image.open(image_stream)
    return predict(image, variant, instruction)


predict_numericalmatch = NumericalmatchPredictor().predict

# will be removed later
predict_3d_rollball_animals = lambda image: predict(image, '3d_rollball_animals')
predict_hopscotch_highsec = lambda image: predict(image, 'hopscotch_highsec')
predict_3d_rollball_objects = lambda image: predict(image, '3d_rollball_objects')
predict_coordinatesmatch = lambda image: predict(image, 'coordinatesmatch')
predict_train_coordinates = lambda image: predict(image, 'train_coordinates')
predict_dicematch = lambda image: predict(image, 'dicematch')

predict_penguins = lambda image: predict(image, 'penguins')
predict_shadows = lambda image: predict(image, 'shadows')
