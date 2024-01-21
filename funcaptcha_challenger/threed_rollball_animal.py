from funcaptcha_challenger.threed_rollball_objects import ThreeDRollballObjectsPredictor


class ThreeDRollballAnimalPredictor(ThreeDRollballObjectsPredictor):

    def is_support(self, variant, instruction):
        return '3d_rollball_animals' == variant
