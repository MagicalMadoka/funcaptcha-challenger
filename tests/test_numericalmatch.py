import os
import unittest

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict_numericalmatch
from tests.utils import get_ans_from_image_name


class TestMatchCount(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.images_path = os.path.join(this_dir, '../demo', 'captcha-images','numericalmatch')

    def test_predict(self):
        images_name = os.listdir(self.images_path)

        for image_name in images_name:
            logger.info(f'test match count image name is {image_name}')
            image_path = os.path.join(self.images_path, image_name)
            image = Image.open(image_path)
            index = predict_numericalmatch(image)
            self.assertEqual(index, get_ans_from_image_name(image_name))