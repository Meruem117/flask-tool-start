from flask import Flask, escape, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Flask"


@app.route('/user/<string:username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


with app.test_request_context():
    url_for('static', filename='style.css')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)
        return render_template('form.html')


if __name__ == '__main__':
    app.run()
