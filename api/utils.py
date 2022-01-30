import os
import cv2
import numpy as np


def write_to_tmp(file):
    file_path = f'temp/{file}'
    with open(file_path, 'wb+') as f:
        f.write(file.read())
    print(f'File added :{file_path}')
    return file_path


def serializeImg(img):
    image = cv2.imdecode(np.frombuffer(img.read(), np.uint8), cv2.IMREAD_COLOR)
    _, img_buffer_arr = cv2.imencode(".jpg", image)
    img_bytes = img_buffer_arr.tobytes()
    print(len(img_bytes))
    return img_bytes


def remove_from_tmp(file_path):
    os.remove(file_path)
    print(f'File removed :{file_path}')


def upload_to_storage(file_path):

    return file_path
