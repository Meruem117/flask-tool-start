from flask import Flask, request, render_template
from modules.forms import ImageForm
from modules.image import image_tmp_save, image_to_ico, image_tmp_delete
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def image_page():
    if request.method == 'POST':
        form = ImageForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            image = form.image.data
            title = form.title.data
            print(title)
    return render_template('image.html')


if __name__ == '__main__':
    app.run()
