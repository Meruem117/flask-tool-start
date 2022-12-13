from flask import Flask, render_template
from flask_wtf import CSRFProtect
from modules.forms import ImageForm
from modules.image import image_tmp_save, image_to_ico, image_tmp_delete
from modules.mysql import show_database, show_tables, show_table_columns, select_table_data

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


@app.route('/db', methods=['GET'])
@app.route('/db/<string:database_name>', methods=['GET'])
@app.route('/db/<string:database_name>/<string:table_name>', methods=['GET'])
def db_page(database_name=None, table_name=None):
    database_list = show_database()
    table_list = []
    column_list = []
    data_list = []
    if database_name is not None:
        table_list = show_tables(database_name)
        if table_name is not None:
            column_list = show_table_columns(database_name, table_name)
            data_list = select_table_data(database_name, table_name)
    return render_template('db.html', database_list=database_list, database_name=database_name,
                           table_list=table_list, table_name=table_name,
                           column_list=column_list,
                           data_list=data_list)


if __name__ == '__main__':
    app.run()
