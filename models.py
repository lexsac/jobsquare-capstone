"""SQLAlchemy models for my job board."""

import datetime
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    location = db.Column(db.Text, nullable=True)
    category = db.Column(db.Text, nullable=True)
    experience_level = db.Column(db.Text, nullable=True)
    company = db.Column(db.Text, nullable=True)

    jobs_liked = db.relationship("Job", secondary="users_jobs", backref="users_liked")

    @classmethod
    def signup(cls, first_name, last_name, email, username, password, location, category, experience_level, company):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=hashed_pwd,
            location=location,
            category=category,
            experience_level=experience_level,
            company=company
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


class Job(db.Model):
    """Job post."""

    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text, nullable=False)
    experience_level = db.Column(db.Text, nullable=False)
    company = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    landing_page_url = db.Column(db.Text, nullable=False)


class UserJob(db.Model):
    """List of jobs liked by users."""

    __tablename__ = "users_jobs"

    user_id = db.Column(
        db.Integer, 
        db.ForeignKey('users.id', ondelete="cascade"),
        primary_key=True
    )
    job_id = db.Column(
        db.Integer, 
        db.ForeignKey('jobs.id', ondelete="cascade"),
        primary_key=True
    )


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
