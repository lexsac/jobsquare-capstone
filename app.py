import os

from flask import Flask, request, redirect, render_template, flash, g, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Job
from sqlalchemy.exc import IntegrityError
import requests
from key import API_SECRET_KEY
from forms import UserAddForm, UserEditForm, LoginForm

API_BASE_URL = "https://www.themuse.com/api/public/jobs"
CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///job_board'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)


def get_jobs(location, company, category, experience_level):
    res = requests.get(f"{API_BASE_URL}?page=1",
        params={"key": API_SECRET_KEY,
                "location": location,
                "company": company,
                "category": category,
                "level": experience_level    
        })
    data = res.json()
    return data['results']



##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                first_name= form.first_name.data,
                last_name= form.last_name.data,
                email=form.email.data,
                username=form.username.data,
                password=form.password.data,
                location = form.location.data,
                category = form.category.data,
                experience_level = form.experience_level.data,
                company = form.company.data
            )
            db.session.commit()

        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")


##############################################################################
# General user routes:

@app.route('/users/likes', methods=["GET"])
def show_likes(user_id):
    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = User.query.get_or_404(user_id)
    return render_template('users/likes.html', user=user, likes=user.jobs_liked)


# @app.route('/jobs/<int:job_id>/like', methods=['POST'])
# def add_like(job_id):
#     """Toggle a liked job for the currently-logged-in user."""

#     if not g.user:
#         flash("Access unauthorized.", "danger")
#         return redirect("/")

#     liked_job = Job.query.get_or_404(job_id)
#     if liked_job.user_id == g.user.id:
#         return abort(403)

#     user_likes = g.user.likes

#     if liked_job in user_likes:
#         g.user.likes = [like for like in user_likes if like != liked_message]
#     else:
#         g.user.likes.append(liked_message)

#     db.session.commit()

#     return redirect("/")


@app.route('/users/profile', methods=["GET", "POST"])
def edit_profile():
    """Update profile for current user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = g.user
    form = UserEditForm(obj=user)

    if form.validate_on_submit():
        if User.authenticate(user.username, form.password.data):
            first_name= form.first_name.data,
            last_name= form.last_name.data,
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
            location = form.location.data,
            category = form.category.data,
            experience_level = form.experience_level.data,
            company = form.company.data

            db.session.commit()
            return redirect("/")

        flash("Wrong password, please try again.", 'danger')

    return render_template('users/edit.html', form=form, user_id=user.id)


# @app.route('/users/delete', methods=["POST"])
# def delete_user():
#     """Delete user."""

#     if not g.user:
#         flash("Access unauthorized.", "danger")
#         return redirect("/")

#     do_logout()

#     db.session.delete(g.user)
#     db.session.commit()

#     return redirect("/signup")


##############################################################################
# Jobs routes:

@app.route('/jobs/<int:job_id>', methods=["GET"])
def jobs_show(job_id):
    """Show a job."""

    job = Job.query.get_or_404(job_id)
    return render_template('jobs/detail.html', job=job)


##############################################################################
# Homepage and error pages

@app.route('/')
def homepage():
    """Show homepage:

    - anon users: no messages
    - logged in: 100 most recent messages of followed_users
    """

    if g.user:
        
        location = g.user.location
        company = g.user.company
        category = g.user.category
        experience_level = g.user.experience_level

        jobs = get_jobs(location, company, category, experience_level)

        return render_template('home.html', jobs=jobs)

    else:
        return render_template('home-anon.html')


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404