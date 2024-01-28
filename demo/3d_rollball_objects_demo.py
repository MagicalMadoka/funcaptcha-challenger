import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', '3d_rollball_objects', '9788bc0dc2c14258b032b06eccbc7b50_3.jpg')

image = Image.open(image_path)

index = predict(image, '3d_rollball_objects')
logger.info(f"Predicted index: {index}")
