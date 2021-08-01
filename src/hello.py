from flask import Flask, escape, url_for, request, render_template

app = Flask(__name__)


# route
@app.route('/')
def index():
    return "Hello Flask ~"


# 重定向url
@app.route('/about')
def about():
    return 'The about page'


@app.route('/projects/')
def projects():
    return 'The project page'


# url变量
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


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('about', detail='p1'))
#     print(url_for('show_user_profile', username='John Doe'))

# HTTP request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return about()
    else:
        return show_user_profile('John')


# 静态文件
with app.test_request_context():
    url_for('static', filename='style.css')


# 渲染模板
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
