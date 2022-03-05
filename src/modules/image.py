from wand.image import Image
import os
import datetime


def image_save(image):
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    old_names = os.path.splitext(image.filename)
    new_name = old_names[0] + '-' + now + old_names[1]
    par_dir = os.path.pardir
    cur_dir = os.path.dirname(__file__)
    src_dir = os.path.abspath(os.path.join(cur_dir, par_dir))
    tmp_path = os.path.join(src_dir + '/static/tmp', new_name)
    image.save(tmp_path)
    return new_name


def image_to_ico(image: str):
    with Image(filename=image) as original:
        with original.convert('ico') as converted:
            return converted
