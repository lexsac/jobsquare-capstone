from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SearchField
from wtforms.validators import DataRequired, Email, Length, Optional
from models import Location, Company, Experiencelevel, User

locations_list = ['Abu Dhabi, United Arab Emirates', 'Adana, Turkey', 'Aix-en-Provence, France', 'Alcoa, TN', 'Algiers, Algeria', 'Almaty, Kazakhstan', 'Ann Arbor, MI', 'Aurangabad, India', 'Austin, TX', 'Bad Mergentheim, Germany', 'Bad Neustadt an der Saale, Germany', 'Baltimore, MD', 'Bangalore, India', 'Bangkok, Thailand', 'Barcelona, Spain', 'Beijing, China', 'Beja, Portugal', 'Bellevue, WA', 'Berlin, Germany', 'Bexley, United Kingdom', 'Bezons, France', 'Bloomington, IL', 'Blue Ash, OH', 'Bratislava, Slovakia', 'Braunschweig, Germany', 'Braşov, Romania', 'Bremen, Germany', 'Brentford, United Kingdom', 'Broken Arrow, OK', 'Brussels, Belgium', 'Bucharest, Romania', 'Budapest, Hungary', 'Buenos Aires, Argentina', 'Buffalo Grove, IL', 'Cairo, Egypt', 'Cary, NC', 'Casablanca, Morocco', 'Changchun, China', 'Charlotte, NC', 'Chemnitz, Germany', 'Chengdu, China', 'Chennai, India', 'Chicago, IL', 'Chippenham, United Kingdom', 'Cincinnati, OH', 'Clayton, NC', 'Coburg, Germany', 'Coimbra, Portugal', 'Cologne, Germany', 'Colorado Springs, CO', 'Dalian, China', 'Des Moines, IA', 'Doha, Qatar', 'Dombivli, India', 'Dresden, Germany', 'Dubuque, IA', 'Durham, NC', 'Entroncamento, Portugal', 'Erlangen, Germany', 'Fairbanks, AK', 'Flexible / Remote', 'Forchheim, Germany', 'Forst, Germany', 'Frankfurt, Germany', 'Freiburg, Germany', 'Fremont, CA', 'Fribourg, Switzerland', 'Fürth, Germany', 'Gainesville, FL', 'Gdańsk, Poland', 'Griesheim, Germany', 'Guadalajara, Mexico', 'Gurgaon, India', 'Guyancourt, France', 'Guéret, France', 'Hamburg, Germany', 'Hinganghāt, India', 'Hong Kong', 'Illkirch-Graffenstaden, France', 'Indianapolis, IN', 'Innsbruck, Austria', 'Istanbul, Turkey', 'Jacksonville, FL', 'Johnson City, TN', 'Jundiaí, Brazil', 'Kansas City, KS', 'Karlovy Vary, Czech Republic', 'Karlsruhe, Germany', 'Katowice, Poland', 'Kingston upon Hull, United Kingdom', 'Koblenz, Germany', 'Konstanz, Germany', 'Kopřivnice, Czech Republic', 'Košice, Slovakia', 'Krakow, Poland', 'Kriens, Switzerland', 'Kuala Lumpur, Malaysia', 'Kutná Hora, Czech Republic', 'Lafayette, LA', 'Lake Oswego, OR', 'Lakewood, NJ', 'Larkhall, United Kingdom', 'Limbach-Oberfrohna, Germany', 'Lincoln, United Kingdom', 'Lindau, Germany', 'Lisbon, Portugal', 'London, Canada', 'London, United Kingdom', 'Los Angeles, CA', 'Lublin, Poland', 'Luzern, Switzerland', 'Lyon, France', 'Madison, WI', 'Madrid, Spain', 'Malvern, PA', 'Manchester, United Kingdom', 'Manila, Philippines', 'Marktredwitz, Germany', 'Milan, Italy', 'Mishawaka, IN', 'Mobile, AL', 'Montreal, Canada', 'Mt. Vernon, WA', 'Mumbai, India', 'Munich, Germany', 'Muttenz, Switzerland', 'Mühlhausen, Germany', 'Nanchang, China', 'Nanjing, China', 'Neue Neustadt, Germany', 'Noida, India', 'Norcross, GA', 'Norrtälje, Sweden', 'Northampton, United Kingdom', 'Norwood, MA', 'Nürnberg, Germany', 'Oisterwijk, Netherlands', 'Orlando, FL', 'Oslo, Norway', 'Ostrava, Czech Republic', 'Ottawa, Canada', 'Paris, France', 'Pasadena, CA', 'Peoria, IL', 'Phoenix, AZ', 'Pilsen, Czech Republic', 'Plovdiv, Bulgaria', 'Portsmouth, NH', 'Prague, Czech Republic', 'Pune, India', 'Raleigh, NC', 'Reedley, CA', 'Regensburg, Germany', 'Richmond, VA', 'Riyadh, Saudi Arabia', 'Roanne, France', 'Rochester, United Kingdom', 'Rolling Meadows, IL', 'Río Grande, Mexico', 'Sacramento, CA', 'San Diego, CA', 'Santarém, Portugal', 'Schaumburg, IL', 'Scottsdale, AZ', 'Seattle, WA', 'Sebring, FL', 'Secaucus, NJ', 'Selby, United Kingdom', 'Seongnam-si, South Korea', 'Seoul, South Korea', 'Shanghai, China', 'Shenzhen, China', 'Sibiu, Romania', 'Silkeborg, Denmark', 'Sindelfingen, Germany', 'Sofia, Bulgaria', 'Spartanburg, SC', 'Spring House, PA', 'St. Louis, MO', 'State College, PA', 'Stuttgart, Germany', 'Sydney, Australia', 'Syracuse, NY', 'Szeged, Hungary', 'São Paulo, Brazil', 'Tarrytown, NY', 'Tempe, AZ', 'The Hague, Netherlands', 'Tianjin, China', 'Tokyo, Japan', 'Toulouse, France', 'United States', 'Upper Alton, IL', 'Varna, Bulgaria', 'Vienna, Austria', 'Virginia Beach, VA', 'Waltham, MA', 'Washington, DC', 'Weingarten, Germany', 'Weston, MA', 'Wroclaw, Poland', 'Wuxi, China', 'Zurich, Switzerland', 'Évry, France', 'Łódź, Poland', 'Šumperk, Czech Republic']

class UserAddForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    location = SelectField('Location', choices=locations_list)
    category = SelectField('Category', choices=[('Software Engineering', 'Software Engineering')])
    experience_level = SelectField('Experience Level', choices=[('Internship'), ('Entry Level'), ('Mid Level'), ('Senior Level')])
    company = SelectField('Company', choices=[('Siemens'), ('Echo Global Logistics')])
    
class UserEditForm(FlaskForm):
    """Form for editing users."""

    password = PasswordField('Password', validators=[Length(min=6)])
    location = SelectField('Location', choices=locations_list)
    category = SelectField('Category', choices=[('Software Engineering', 'Software Engineering')])
    experience_level = SelectField('Experience Level', choices=[('Internship'), ('Entry Level'), ('Mid Level'), ('Senior Level')])
    company = SelectField('Company', choices=[('Siemens'), ('Echo Global Logistics')])

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


