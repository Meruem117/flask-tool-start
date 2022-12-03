from flask import Flask, render_template
from flask_wtf import CSRFProtect
from modules.forms import ImageForm
from modules.image import image_tmp_save, image_to_ico, image_tmp_delete
from modules.mysql import select_table_data

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


@app.route('/table/<string:table_name>', methods=['GET'])
def select_table(table_name):
    list = select_table_data(table_name)
    return render_template('table.html', list=list)


if __name__ == '__main__':
    app.run()
