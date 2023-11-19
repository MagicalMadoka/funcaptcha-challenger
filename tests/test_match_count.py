import os
import unittest

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict_count_match_image
from tests.utils import get_ans_from_image_name


class TestMatchCount(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.images_path = os.path.join(this_dir, '../demo', 'captcha-images','match-count')

    def test_predict(self):
        images_name = os.listdir(self.images_path)

        for image_name in images_name:
            logger.info(f'test match count image name is {image_name}')
            image_path = os.path.join(self.images_path, image_name)
            image = Image.open(image_path)
            index = predict_count_match_image(image)
            self.assertEqual(index, get_ans_from_image_name(image_name))