from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SearchField
from wtforms.validators import DataRequired, Email, Length, Optional
from models import Location, Company, Experiencelevel, User, Category

with open('locations.txt', 'r') as file:
    # Read the lines of locations.txt and store them in a list
    lines = file.readlines()

    # Remove any whitespace characters from each line
    lines = [line.strip() for line in lines]

    # Sort the lines alphabetically
    lines.sort()

    # Create an empty array to store the items
    items = []

    # Loop through each line and add it to the array
    for line in lines:
        items.append(line)

location_list = items
category_list = ['Account Management', 'Accounting and Finance', 'Administration and Office', 'Advertising and Marketing', 'Arts', 'Business Operations', 'Cleaning and Facilities', 'Computer and IT', 'Construction', 'Customer Service', 'Data and Analytics', 'Design and UX', 'Education', 'Energy Generation and Mining', 'Entertainment and Travel Services', 'Farming and Outdoors', 'Food and Hospitality Services', 'Healthcare', 'Human Resources and Recruitment', 'Installation, Maintenance, and Repairs', 'Legal Services', 'Management', 'Manufacturing and Warehouse', 'Media, PR, and Communications', 'Product Management', 'Project Management', 'Protective Services', 'Real Estate', 'Retail', 'Sales', 'Science and Engineering', 'Social Services', 'Software Engineering', 'Transportation and Logistics', 'Writing and Editing']
experience_level_list = ['Entry Level', 'Internship', 'Mid Level', 'Senior Level']
company_list = ['Echo Global Logistics', 'Merge', 'Philips', 'Siemens', 'Sotheby\'s', 'SpaceX']

class UserAddForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

    # location = SelectField(
    #     'Select a location', 
    #     choices=location_list, 
    #     validators=[DataRequired()])

    # category = SelectField(
    #     'Select a job category',
    #     choices=category_list,
    #     validators=[DataRequired()]
    # )
    
    # experience_level = SelectField(
    #     'Experience Level', 
    #     choices=experience_level_list,
    #     validators=[DataRequired()]
    # )
    
    # company = SelectField(
    #     'Company', 
    #     choices=company_list,
    #     validators=[DataRequired()]
    # )
    

class UserEditForm(FlaskForm):
    """Form for editing users."""

    password = PasswordField('Password', validators=[Length(min=6)])
    # location = SelectField(
    #     'Select a location', 
    #     choices=location_list, 
    #     validators=[DataRequired()])

    # category = SelectField(
    #     'Select a job category',
    #     choices=category_list,
    #     validators=[DataRequired()]
    # )
    
    # experience_level = SelectField(
    #     'Experience Level', 
    #     choices=experience_level_list,
    #     validators=[DataRequired()]
    # )
    
    # company = SelectField(
    #     'Company', 
    #     choices=company_list,
    #     validators=[DataRequired()]
    # )
    

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


