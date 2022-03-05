from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/image', methods=['GET', 'POST'])
def image_page():
    if request.method == 'GET':
        return render_template('image.html')
    else:
        return 'Submit'


if __name__ == '__main__':
    app.run()
