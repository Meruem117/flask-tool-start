from wand.image import Image
import os
import datetime


def image_tmp_save(image):
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    old_names = os.path.splitext(image.filename)
    new_name = old_names[0] + '-' + now + old_names[1]
    par_dir = os.path.pardir
    cur_dir = os.path.dirname(__file__)
    src_dir = os.path.abspath(os.path.join(cur_dir, par_dir))
    tmp_path = os.path.join(src_dir + '/static/tmp', new_name)
    image.save(tmp_path)
    return tmp_path, old_names[0]


def image_to_ico(image, name, size):
    with Image(filename=image) as img:
        img.resize(size, size)
        img.format = 'ico'
        img.save(filename='tmp/' + name + '.ico')


def image_tmp_delete(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        print('File not exists')
