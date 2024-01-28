import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'train_coordinates',
                          '2024-01-19 08.25.35_5.jpg')

image = Image.open(image_path)

index = predict(image, 'train_coordinates')
logger.info(f"Predicted index: {index}")
