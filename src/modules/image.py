from wand.image import Image
import os
import datetime


def image_tmp_save(image):
    now = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    tmp_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + '\\static\\tmp'
    tmp_path = os.path.join(tmp_dir, now + image.filename)
    image.save(tmp_path)
    return tmp_path


def image_to_ico(image, name, size):
    # save to desktop
    # name += '.ico'
    # path = os.path.join(os.path.expanduser('~'), 'Desktop')
    # dev tmp save
    name = os.path.splitext(image)[0] + '.ico'
    # name = os.path.splitext(image)[0].split('\\')[-1][20:] + '.ico'
    with Image(filename=image) as img:
        img.resize(size, size)
        img.format = 'ico'
        # img.save(filename=os.path.join(path, name))
        img.save(filename=name)


def image_tmp_delete(image):
    try:
        os.remove(image)
    except FileNotFoundError:
        print('File not exists')
