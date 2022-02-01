from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ijk'


class Register(FlaskForm):
    username = StringField(label='username', validators=[DataRequired('username can not be null')])
    password = PasswordField(label='password', validators=[DataRequired('password can not be null')])
    password_check = PasswordField(label='password check', validators=[DataRequired('password check can not be null')])
    submit = SubmitField(label='submit')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            password_check = form.password_check.data
            print(username, password, password_check)
        else:
            print('validate fail')
        return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run()
