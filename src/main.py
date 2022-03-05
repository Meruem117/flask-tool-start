from flask import Flask, request, render_template
from forms import ImageForm
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
            print(image)
            return 'Success'


if __name__ == '__main__':
    app.run()
