from funcaptcha_challenger.hopscotch_highsec import HopscotchHighsecPredictor
from funcaptcha_challenger.numericalmatch import NumericalmatchPredictor
from funcaptcha_challenger.rotate_animal import AnimalRotationPredictor

arp = AnimalRotationPredictor()
predict_3d_rollball_animals = arp.predict

ocp = NumericalmatchPredictor()
predict_numericalmatch = ocp.predict

phh = HopscotchHighsecPredictor()

predict_hopscotch_highsec = phh.predict
