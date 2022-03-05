from wand.image import Image
import os


def image_save(image, path: str = None):
    if path is None:
        par_dir = os.path.pardir
        cur_dir = os.path.dirname(__file__)
        tmp_dir = os.path.abspath(os.path.join(cur_dir, par_dir)) + '\\tmp'
        image.save(tmp_dir, image.filename)


def image_to_ico(image: str):
    with Image(filename=image) as original:
        with original.convert('ico') as converted:
            return converted
