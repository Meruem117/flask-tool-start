from flask import Flask, render_template, send_from_directory
from flask_wtf import CSRFProtect
from modules.forms import ImageForm
from modules.image import image_tmp_save, image_to_ico, image_tmp_delete

app = Flask(__name__)
CSRFProtect(app)
app.config['SECRET_KEY'] = 'flask-tool-start'


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def image_page():
    form = ImageForm()
    if form.validate_on_submit():
        image = form.image.data
        title = form.title.data
        size = form.size.data
        image_path = image_tmp_save(image)
        image_to_ico(image_path, title, int(size))
        image_tmp_delete(image_path)
    else:
        print(form.errors)
    return render_template('image.html', form=form)


if __name__ == '__main__':
    app.run()
