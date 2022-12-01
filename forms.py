from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional


class UserAddForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    location = SelectField('Location', choices=[('New York, NY', 'New York, NY'), ('Los Angeles, CA', 'Los Angeles, CA')])
    category = SelectField('Category', choices=[('Software Engineering', 'Software Engineering'), ('Product Strategy', 'Product Strategy'), ('Business Operations', 'Business Operations')])
    experience_level = SelectField('Experience Level', choices=[('Entry Level', 'Entry Level'), ('Mid Level', 'Mid Level')])
    company = SelectField('Company', choices=[('Google', 'Google'), ('Apple', 'Apple')])


class UserEditForm(FlaskForm):
    """Form for editing users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    image_url = StringField('(Optional) Image URL')
    header_image_url = StringField('(Optional) Header Image URL')
    bio = TextAreaField('(Optional) Tell us about yourself')
    password = PasswordField('Password', validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])