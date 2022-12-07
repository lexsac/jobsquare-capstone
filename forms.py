from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SearchField
from wtforms.validators import DataRequired, Email, Length, Optional


class UserAddForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    location_id = SelectField('Location', choices=[('1', '1'), ('2', '2')])
    
    # def edit_location(request, id):
    # job_location = Job.query.get(id)
    # form = UserAddForm(request.POST, obj=job_location)
    # form.location.choices = [(l.id, l.name) for l in Location.query.order_by('name')]

    category_id = SelectField('Category', choices=[('1', '1'), ('2', '2')])
    experience_level_id = SelectField('Experience Level', choices=[('1', '1'), ('2', '2')])
    company_id = SelectField('Company', choices=[('1', '1'), ('2', '2')])


class UserEditForm(FlaskForm):
    """Form for editing users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    location_id = SelectField('Location', choices=[('New York, NY', 'New York, NY'), ('Los Angeles, CA', 'Los Angeles, CA')])
    category_id = SelectField('Category', choices=[('Software Engineering', 'Software Engineering'), ('Product Strategy', 'Product Strategy'), ('Business Operations', 'Business Operations')])
    experience_level_id = SelectField('Experience Level', choices=[('Entry Level', 'Entry Level'), ('Mid Level', 'Mid Level')])
    company_id = SelectField('Company', choices=[('Google', 'Google'), ('Apple', 'Apple')])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])