"""User model tests."""

# to run these tests: python -m unittest test_user_model.py


import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User

# set an environmental variable to use a different database for tests 
# (we need to do this before we import our app, since that will have already
# connected to the database)

os.environ['DATABASE_URL'] = "postgresql:///job_board_test"

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()

        u1 = User.signup("anne", "anne","anne@email.com", "anne1234", "password")
        # uid1 = 1
        # u1.id = uid1

        u2 = User.signup("joe", "joe","joe@email.com", "joe1234", "password")
        # uid2 = 2
        # u2.id = uid2

        db.session.commit()

        u1 = User.query.get(1)
        u2 = User.query.get(2)

        self.u1 = u1
        self.uid1 = 1

        self.u2 = u2
        self.uid2 = 2

        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            first_name="test",
            last_name="test",
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no liked jobs
        self.assertEqual(len(u.likes), 0)

    ####
    #
    # Signup Tests
    #
    ####
    # def test_valid_signup(self):
    #     with app.app_context():
    #         u_test = User.signup("julie", "jones", "julie@test.com", "julie1234", "password")
    #         uid = 99999
    #         u_test.id = uid
    #         db.session.commit()

            # u_test = User.query.get(uid)
            # self.assertIsNotNone(u_test)
            # self.assertEqual(u_test.first_name, "julie")
            # self.assertEqual(u_test.last_name, "jones")
            # self.assertEqual(u_test.username, "julie1234")
            # self.assertEqual(u_test.email, "julie@test.com")
            # self.assertNotEqual(u_test.password, "password")
            # # Bcrypt strings should start with $2b$
            # self.assertTrue(u_test.password.startswith("$2b$"))

    def test_invalid_username_signup(self):
        """Does adding an invalid username cause an expected error?"""

        invalid = User.signup("Maria", "Maria", "test@test.com", None, "password")
        uid = 123456
        invalid.id = uid
        with self.assertRaises(exc.IntegrityError) as context:
            db.session.commit()

    def test_invalid_email_signup(self):
        invalid = User.signup("sam", "sam", None, "sam1234", "password")
        uid = 123789
        invalid.id = uid
        with self.assertRaises(exc.IntegrityError) as context:
            db.session.commit()
    
    ####
    #
    # Authentication Tests
    #
    ####
    def test_valid_authentication(self):
        u = User.authenticate(self.u1.username, "password")
        self.assertIsNotNone(u)
        self.assertEqual(u.id, self.uid1)
    
    def test_invalid_username(self):
        self.assertFalse(User.authenticate("badusername", "password"))

    def test_wrong_password(self):
        self.assertFalse(User.authenticate(self.u1.username, "badpassword"))




        




        

