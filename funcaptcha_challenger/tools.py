import numpy as np


def check_image_pair_classifier_image_size(image):
    if image.height != 400 or image.width % 200 != 0:
        raise ValueError("Image size must be (n * 200) x 400 pixels")


def check_image_classifier_image_size(image):
    if image.height != 200 or image.width != 300:
        raise ValueError("Image size must be 300 x 200 pixels")


def process_pair_classifier_image(image, index, input_shape=(52, 52), is_grayscale=False):
    x, y = index[1] * 200, index[0] * 200
    sub_image = image.crop((x, y, x + 200, y + 200)).resize(input_shape)

    if is_grayscale:
        sub_image = sub_image.convert('L')
        return np.array(sub_image)[np.newaxis, np.newaxis, ...] / 255.0

    return np.array(sub_image).transpose(2, 0, 1)[np.newaxis, ...] / 255.0


def process_image_classifier_image(image, index, input_shape=(52, 52), is_grayscale=False):
    target_img = crop_funcaptcha_image(image, (index // 3, index % 3), width=100).resize(input_shape)
    if is_grayscale:
        target_img = target_img.convert('L')
        return np.array(target_img)[np.newaxis, np.newaxis, ...] / 255.0
    return np.array(target_img).transpose(2, 0, 1)[np.newaxis, ...] / 255.0


def process_pair_classifier_ans_image(image, input_shape=(52, 52), is_grayscale=False):
    sub_image = crop_funcaptcha_ans_image(image).resize(input_shape)
    if is_grayscale:
        sub_image = sub_image.convert('L')
        return np.array(sub_image)[np.newaxis, np.newaxis, ...] / 255.0

    return np.array(sub_image).transpose(2, 0, 1)[np.newaxis, ...] / 255.0


def crop_funcaptcha_image(image, index, width=200):
    x, y = index[1] * width, index[0] * width
    return image.crop((x, y, x + width, y + width))


def crop_funcaptcha_ans_image(image):
    return image.crop((0, 200, 135, 400))


def crop_image_to_box(image, box):
    x_min, y_min, x_max, y_max = [int(coordinate[0]) for coordinate in box[:4]]

    return image.crop((x_min, y_min, x_max, y_max))
