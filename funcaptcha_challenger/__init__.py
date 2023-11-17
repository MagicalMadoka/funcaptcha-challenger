from funcaptcha_challenger.match_count import ObjectCountPredictor
from funcaptcha_challenger.rotate_animal import AnimalRotationPredictor

arp = AnimalRotationPredictor()
predict_animal_rotation_towards_hand = arp.predict

ocp = ObjectCountPredictor()
predict_count_match_image = ocp.predict
