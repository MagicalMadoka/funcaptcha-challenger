import numpy as np

from funcaptcha_challenger.model import BaseModel
from funcaptcha_challenger.tools import check_input_image_size, process_image, crop_funcaptcha_image, crop_image_to_box


def parse_row(row, img_width=200, img_height=200):
    xc, yc, w, h = row[:4]
    x1 = (xc - w / 2) / 224 * img_width
    y1 = (yc - h / 2) / 224 * img_height
    x2 = (xc + w / 2) / 224 * img_width
    y2 = (yc + h / 2) / 224 * img_height
    prob = row[4:].max()
    class_id = row[4:].argmax()
    label = class_id
    return [x1, y1, x2, y2, label, prob]


def intersection(box1, box2):
    box1_x1, box1_y1, box1_x2, box1_y2 = box1[:4]
    box2_x1, box2_y1, box2_x2, box2_y2 = box2[:4]
    x1 = max(box1_x1, box2_x1)
    y1 = max(box1_y1, box2_y1)
    x2 = min(box1_x2, box2_x2)
    y2 = min(box1_y2, box2_y2)
    return (x2 - x1) * (y2 - y1)


def union(box1, box2):
    box1_x1, box1_y1, box1_x2, box1_y2 = box1[:4]
    box2_x1, box2_y1, box2_x2, box2_y2 = box2[:4]
    box1_area = (box1_x2 - box1_x1) * (box1_y2 - box1_y1)
    box2_area = (box2_x2 - box2_x1) * (box2_y2 - box2_y1)
    return box1_area + box2_area - intersection(box1, box2)


def iou(box1, box2):
    return intersection(box1, box2) / union(box1, box2)


def determine_left_right(box1, box2):
    # 计算每个框的中心点 x 坐标
    center_x1 = (box1[0] + box1[2]) / 2
    center_x2 = (box2[0] + box2[2]) / 2

    # 比较中心点 x 坐标
    if center_x1 < center_x2:
        return box1, box2
    else:
        return box2, box1


class ObjectCountPredictor:
    def __init__(self):
        self.source_detection_model = BaseModel("match_count_source_detection.onnx")
        self.target_detection_model = BaseModel("match_count_target_detection.onnx")
        self.similarity_model = BaseModel("match_count_similarity.onnx")

    def predict(self, image) -> int:
        check_input_image_size(image)

        target = process_image(image, (1, 0), (224, 224))
        result = self._target_boxs(target, self.source_detection_model)

        if len(result) != 2:
            raise ValueError("predict fail")

        count_box, source_box = determine_left_right(result[0], result[1])
        count = count_box[4]

        source_image = crop_image_to_box(crop_funcaptcha_image(image, (1, 0)), source_box)
        source_image = np.array(source_image.resize((52, 52))).transpose(2, 0, 1)[np.newaxis, ...] / 255.0

        width = image.width
        for i in range(width // 200):
            im = crop_funcaptcha_image(image, (0, i))

            target_image = process_image(image, (0, i), (224, 224))

            source_output = self._target_boxs(target_image, self.target_detection_model)

            cnt = 0
            for box in source_output:

                target_image = crop_image_to_box(im, box)

                target_image = np.array(target_image.resize((52, 52))).transpose(2, 0, 1)[np.newaxis, ...] / 255.0

                output = self.similarity_model.run_prediction(None, {'input_left': source_image.astype(np.float32),
                                                                     'input_right': target_image.astype(np.float32)})[0]

                prob = output[0][0]

                if prob > 0.5:
                    cnt += 1

            if cnt == count:
                return i

    def _target_boxs(self, target, model):
        output = model.run_prediction(None, {'images': target.astype(np.float32)})[0]

        output = output.transpose()

        boxes = [row for row in [parse_row(row) for row in output] if row[5] > 0.5]

        boxes.sort(key=lambda x: x[5], reverse=True)
        result = []
        while len(boxes) > 0:
            result.append(boxes[0])
            boxes = [box for box in boxes if iou(box, boxes[0]) < 0.7]

        return result
