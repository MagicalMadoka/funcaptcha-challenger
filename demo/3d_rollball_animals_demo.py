from PIL import Image
import os

from loguru import logger

from funcaptcha_challenger import predict_3d_rollball_animals

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', '3d_rollball_animals', '0bcc74b7-487c-4db4-8d48-7d2d2091ae23_3.jpg')

image = Image.open(image_path)

index = predict_3d_rollball_animals(image)
logger.info(f"Predicted index: {index}")