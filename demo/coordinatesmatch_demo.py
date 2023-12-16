import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict_coordinatesmatch

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'coordinatesmatch',
                          '0a5c4c9d89d603d0ae4e1167b3afd12eb4654b05accfa33a9491777534674204_4.jpg')

image = Image.open(image_path)

index = predict_coordinatesmatch(image)
logger.info(f"Predicted index: {index}")
