import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'counting',
                          '0a1d5e94-8187-4124-a999-3ab7af6cb5e3.jpg')

image = Image.open(image_path)

index = predict(image, 'counting')
logger.info(f"Predicted index: {index}")
