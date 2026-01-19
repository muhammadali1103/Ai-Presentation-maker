from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField,IntegerField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Optional


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password')  # Add a password field if needed
    submit = SubmitField('Save Changes')

# forms.py
class GenerateForm(FlaskForm):
    presentation_title = StringField('Title', validators=[DataRequired()])
    presenter_name = StringField('Presenter', validators=[DataRequired()])
    number_of_slide = IntegerField('Number of Slides', validators=[DataRequired()])
    user_text = TextAreaField('Enter your Content', validators=[DataRequired()])
    insert_image = BooleanField('Insert Image Automatically')
    template_choice = SelectField('Choose a Template', choices=[('simple', 'Simple'), ('bright_modern', 'Bright Modern'), ('dark_modern', 'Dark Modern')])
    text_limit_per_slide = IntegerField('Text Limit per Slide', validators=[Optional(), DataRequired()])
