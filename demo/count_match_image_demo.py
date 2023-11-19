from PIL import Image
import os

from loguru import logger

from funcaptcha_challenger import predict_count_match_image

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images','match-count', '601655482afe5f988_3.jpg')

image = Image.open(image_path)

index = predict_count_match_image(image)
logger.info(f"Predicted index: {index}")