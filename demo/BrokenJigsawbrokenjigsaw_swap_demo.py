import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'BrokenJigsawbrokenjigsaw_swap',
                          '1_0763dbd0d732075bba1fda9da7046f10.jpg')

image = Image.open(image_path)

index = predict(image, 'BrokenJigsawbrokenjigsaw_swap')
logger.info(f"Predicted index: {index}")
