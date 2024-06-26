from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('id астронавта ', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта ', validators=[DataRequired()])
    username_k = StringField('id капитана', validators=[DataRequired()])
    password_k = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')