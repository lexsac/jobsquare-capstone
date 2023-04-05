"""Message View tests."""

# to run these tests: python -m unittest test_job_views.py



import os
from unittest import TestCase

from models import db, connect_db, Job, User

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


class JobViewTestCase(TestCase):
    """Test views for jobs."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()


        self.testuser = User.signup(first_name="Sandy",
                                    last_name="Sandy",
                                    email="test@test.com",
                                    username="testuser",
                                    password="testuser")
        self.testuser_id = 8989
        self.testuser.id = self.testuser_id

        db.session.commit()

        self.client = app.test_client()
