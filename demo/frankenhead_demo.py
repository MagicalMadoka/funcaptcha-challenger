import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'frankenhead',
                          '0a645367c6d7857122a66b43e9cb6e1d.jpg')

image = Image.open(image_path)

index = predict(image, 'frankenhead')
logger.info(f"Predicted index: {index}")
