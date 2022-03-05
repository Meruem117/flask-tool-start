import os
from PIL import Image


def image_to_ico(image: str, size: int):
    tmp = os.path.splitext(image)
    if tmp[1] == '.jpg' or '.png':
        ico = tmp[0] + '.ico'
        # im = Image.open(os.path.join(input_path, image)).resize(size)
        print(ico)
