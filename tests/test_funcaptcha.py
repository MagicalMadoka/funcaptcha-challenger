import os
import unittest

from PIL import Image

from funcaptcha_challenger import predict_animal_rotation_towards_hand, predict_count_match_image


class TestFuncaptcha(unittest.TestCase):

    def setUp(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.image_path = os.path.join(this_dir, '../demo', 'captcha_images')

    def test_predict_animal_rotation_towards_hand(self):
        image_path = os.path.join(self.image_path, '0bcc74b7-487c-4db4-8d48-7d2d2091ae23_3.jpg')
        image = Image.open(image_path)
        index = predict_animal_rotation_towards_hand(image)
        self.assertEqual(index, 3)

    def test_predict_count_match_image_1(self):
        image_path = os.path.join(self.image_path, '57655483f9ea8848_0.jpg')
        image = Image.open(image_path)
        index = predict_count_match_image(image)
        self.assertEqual(index, 3)

    def test_predict_count_match_image_2(self):
        image_path = os.path.join(self.image_path, '318655482944f5e67_2.jpg')
        image = Image.open(image_path)
        index = predict_count_match_image(image)
        self.assertEqual(index, 4)


    def test_predict_count_match_image_3(self):
        image_path = os.path.join(self.image_path, '327655483f1ed1798_1.jpg')
        image = Image.open(image_path)
        index = predict_count_match_image(image)
        self.assertEqual(index, 1)

