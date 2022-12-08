from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SearchField
from wtforms.validators import DataRequired, Email, Length, Optional
from models import Location, Company, Experiencelevel




class UserAddForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    location = SearchField('Location')
    category = SelectField('Category', choices=[('Software Engineering', 'Software Engineering')])
    experience_level = SelectField('Experience Level', choices=[('Internship'), ('Entry Level'), ('Mid Level'), ('Senior Level')])
    company = SelectField('Company', choices=[('Siemens', 'Siemens')])
    
class UserEditForm(FlaskForm):
    """Form for editing users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    location = SelectField('Location', choices=[('Lisbon, Portugal', 'Lisbon, Portugal')])
    category = SelectField('Category', choices=[('Software Engineering', 'Software Engineering')])
    experience_level = SelectField('Experience Level', choices=[('Entry Level', 'Entry Level')])
    company = SelectField('Company', choices=[('Apple', 'Apple')])

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])