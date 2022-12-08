import os

from flask import Flask, request, redirect, render_template, flash, g, session, current_app, abort
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
# toolbar = DebugToolbarExtension(app)

connect_db(app)


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

@app.route('/likes', methods=["GET"])
def show_likes():
    """Show liked jobs for current user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = User.query.get_or_404(g.user.id)
    liked_job_ids = [job.id for job in g.user.likes]

    return render_template('users/likes.html', user=user, likes=user.likes, liked_jobs=liked_job_ids)


@app.route('/profile', methods=["GET", "POST"])
def edit_profile():
    """Update profile for current user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = g.user
    form = UserEditForm(obj=user)

    if form.validate_on_submit():
        if User.authenticate(user.username, form.password.data):
            user.first_name = form.first_name.data,
            user.last_name = form.last_name.data,
            user.email =form.email.data,
            user.username = form.username.data,
            user.location = form.location.data,
            user.category = form.category.data,
            user.experience_level = form.experience_level.data,
            user.company = form.company.data

            db.session.commit()
            return redirect("/")

        flash("Wrong password, please try again.", 'danger')

    return render_template('users/edit.html', form=form, user_id=user.id)


@app.route('/delete', methods=["POST"])
def delete_user():
    """Delete user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    do_logout()

    db.session.delete(g.user)
    db.session.commit()

    return redirect("/signup")


##############################################################################
# Jobs routes:

@app.route('/jobs/<int:job_id>', methods=["GET"])
def jobs_show(job_id):
    """Show a job's details."""

    job = Job.query.get_or_404(job_id)
    return render_template('jobs/detail.html', job=job)


@app.route('/jobs/<int:job_id>/like', methods=['POST'])
def add_like(job_id):
    """Toggle a liked job for the currently-logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    liked_job = Job.query.get_or_404(job_id)
    user_likes = g.user.likes

    if liked_job in user_likes:
        g.user.likes = [like for like in user_likes if like != liked_job]
    else:
        g.user.likes.append(liked_job)

    db.session.commit()

    return redirect("/")

##############################################################################
# Homepage and error pages

@app.route('/')
def homepage():
    """Show homepage:

    - anon users: no messages
    - logged in: shows jobs that match preference criteria
    """

    if g.user:
        jobs = Job.query.filter(Job.experience_level == g.user.experience_level, 
                                Job.location == g.user.location,
                                # Job.category == g.user.category,
                                Job.company == g.user.company,
                                ).all()
        
        liked_job_ids = [job.id for job in g.user.likes]

        return render_template('home.html', jobs=jobs, likes=liked_job_ids)

    else:
        return render_template('home-anon.html')


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404