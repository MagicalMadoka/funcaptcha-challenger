import os
import unittest

from PIL import Image

from funcaptcha_challenger import predict_3d_rollball_objects
from tests.utils import get_ans_from_image_name


class Test3dRollBallObjects(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.images_path = os.path.join(this_dir, '../demo', 'captcha-images', '3d_rollball_objects')

    def test_predict(self):
        images_name = os.listdir(self.images_path)

        for image_name in images_name:
            with self.subTest(image_name=image_name):
                image_path = os.path.join(self.images_path, image_name)
                image = Image.open(image_path)
                index = predict_3d_rollball_objects(image)
                self.assertEqual(index, get_ans_from_image_name(image_name))
