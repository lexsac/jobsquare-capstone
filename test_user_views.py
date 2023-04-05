"""User View tests."""

# to run these tests: python -m unittest test_user_views.py


import os
from unittest import TestCase

from models import db, connect_db, Job, User, UserJob
from bs4 import BeautifulSoup

# set an environmental variable to use a different database for tests 
# (we need to do this before we import our app, since that will have already
# connected to the database)

os.environ['DATABASE_URL'] = "postgresql:///job_board_test"


# Now we can import app

from app import app, CURR_USER_KEY

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        self.client = app.test_client()

        self.testuser = User.signup(first_name="Jose",
                                    last_name="Jose",
                                    email="test@test.com",
                                    username="testuser",
                                    password="testuser")
        self.testuser_id = 8989
        self.testuser.id = self.testuser_id

        self.u1 = User.signup(first_name="K",
                                last_name="K",
                                email="k@test.com",
                                username="kuser",
                                password="kuser")
        self.u1_id = 778
        self.u1.id = self.u1_id
        self.u2 = User.signup(first_name="L",
                                last_name="L",
                                email="l@test.com",
                                username="luser",
                                password="luser")
        self.u2_id = 884
        self.u2.id = self.u2_id
        self.u3 = User.signup(first_name="M",
                                last_name="M",
                                email="m@test.com",
                                username="muser",
                                password="muser")

        db.session.commit()

    def tearDown(self):
        resp = super().tearDown()
        db.session.rollback()
        return resp


