from flask import Flask, request, render_template
from modules.forms import ImageForm
from modules.image import image_save
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def image_page():
    if request.method == 'GET':
        return render_template('image.html')
    else:
        form = ImageForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            image = form.image.data
            image_save(image)
            # new_image = image_to_ico(image.filename)
            # new_image.save(os.path.join(dir_path + '/static/images', image.filename))
            return "success"


if __name__ == '__main__':
    app.run()
