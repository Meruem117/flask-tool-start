import os
from PIL import Image


def image_to_ico():
    input_path = 'image'
    output_path = 'icon'
    # 获取目录下文件名
    images = os.listdir('image')
    # 图标大小
    size = (256, 256)

    # 给图标文件单独创建一个icon目录
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for image in images:
        # 分离文件名与扩展名
        tmp = os.path.splitext(image)
        # 因为python文件跟图片在同目录，所以需要判断一下
        if tmp[1] == '.png':
            ico = tmp[0] + '.ico'
            # 打开图片并设置大小
            im = Image.open(os.path.join(input_path, image)).resize(size)
            try:
                # 图标文件保存至icon目录
                path = os.path.join(output_path, ico)
                im.save(path)
                print('{} --> {}'.format(image, ico))
            except IOError:
                print('cannot convert ', image)


if __name__ == '__main__':
    image_to_ico()
