import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'hopscotch_highsec',
                          '5fdbc22c-3093-4fbf-a132-fe05f4182018-3_5.jpg')

image = Image.open(image_path)

index = predict(image, 'hopscotch_highsec')
logger.info(f"Predicted index: {index}")
