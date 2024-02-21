import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'rockstack',
                          '9258513.jpg')

image = Image.open(image_path)

index = predict(image, 'rockstack')
logger.info(f"Predicted index: {index}")
