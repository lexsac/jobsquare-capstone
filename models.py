"""SQLAlchemy models for my job board."""

import datetime
from flask_sqlalchemy import SQLAlchemy

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
