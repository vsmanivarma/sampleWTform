from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask_bootstrap import Bootstrap5



app = Flask(__name__)
app.secret_key = "taggedey_le"
bootstrap = Bootstrap5(app)

def validate_email(form, field):
    email = field.data
    if len(email) < 6:
        raise ValidationError("Email must be more than 6 character's long.")
    elif '@' not in email:
        raise ValidationError("Email is not valid. Please check the email entered.")

def validate_password(form,field):
    password = field.data
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long.')
    elif not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least one digit.')
    elif not any(not char.isalnum() for char in password):
        raise ValidationError('Password must contain at least one special character.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), validate_email])
    password = PasswordField('Password', validators=[DataRequired(), validate_password])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data=="abc123@@@":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', login_form=login_form)

if __name__ == '__main__':
    app.run(debug=True)

