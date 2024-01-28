import os
import unittest

from PIL import Image

from funcaptcha_challenger import predict


class TestCoordinatesMatch(unittest.TestCase):

    def setUp(self):
        self.variant = 'coordinatesmatch'
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.images_path = os.path.join(this_dir, '../demo', 'captcha-images', self.variant)

    def test_predict(self):
        images_name = os.listdir(self.images_path)

        for image_name in images_name:
            if '.jpg' not in image_name:
                continue
            with self.subTest(image_name=image_name):
                image_path = os.path.join(self.images_path, image_name)
                ans_path = image_path.replace('jpg', 'txt')
                image = Image.open(image_path)

                with open(ans_path, 'r') as f:
                    ans = int(f.read())

                index = predict(image, self.variant)
                self.assertEqual(index, ans)
