def get_ans_from_image_name(image_name):
    return int(image_name.split('_')[-1].split('.')[0])