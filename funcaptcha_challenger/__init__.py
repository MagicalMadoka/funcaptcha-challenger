from funcaptcha_challenger.coordinatesmatch import CoordinatesMatchPredictor
from funcaptcha_challenger.hopscotch_highsec import HopscotchHighsecPredictor
from funcaptcha_challenger.numericalmatch import NumericalmatchPredictor
from funcaptcha_challenger.penguin import PenguinPredictor
from funcaptcha_challenger.rotate_animal import AnimalRotationPredictor
from funcaptcha_challenger.shadows import ShadowsPredictor
from funcaptcha_challenger.threed_rollball_objects import ThreeDRollballObjectsPredictor

arp = AnimalRotationPredictor()
predict_3d_rollball_animals = arp.predict

ocp = NumericalmatchPredictor()
predict_numericalmatch = ocp.predict

phh = HopscotchHighsecPredictor()

predict_hopscotch_highsec = phh.predict
predict_3d_rollball_objects = ThreeDRollballObjectsPredictor().predict

predict_coordinatesmatch = CoordinatesMatchPredictor().predict

predict_penguin = PenguinPredictor().predict
predict_shadows = ShadowsPredictor().predict
