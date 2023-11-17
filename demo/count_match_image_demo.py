from PIL import Image
import os

from loguru import logger

from funcaptcha_challenger import predict_count_match_image

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha_images', '57655483f9ea8848_0.jpg')

image = Image.open(image_path)

index = predict_count_match_image(image)
logger.info(f"Predicted index: {index}")