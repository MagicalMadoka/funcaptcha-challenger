import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'shadows',
                          '1d5e432bffabb5d6a32cf06381d43003c2d1f4ad380ffe464a6ae7cf60db4e74_2.jpg')

image = Image.open(image_path)

index = predict(image, 'shadows')
logger.info(f"Predicted index: {index}")
