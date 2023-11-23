import numpy as np


def check_input_image_size(image):
    # todo make it generic
    if image.height != 400 or image.width % 200 != 0:
        raise ValueError("Image size must be (n * 200) x 400 pixels")


def process_image(image, index, input_shape=(52, 52)):
    # todo make it generic
    x, y = index[1] * 200, index[0] * 200
    sub_image = image.crop((x, y, x + 200, y + 200)).resize(input_shape)
    return np.array(sub_image).transpose(2, 0, 1)[np.newaxis, ...] / 255.0


def crop_funcaptcha_image(image, index):
    x, y = index[1] * 200, index[0] * 200
    return image.crop((x, y, x + 200, y + 200))


def crop_image_to_box(image, box):
    x_min, y_min, x_max, y_max = [int(coordinate[0]) for coordinate in box[:4]]

    return image.crop((x_min, y_min, x_max, y_max))
