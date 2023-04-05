"""Job model tests."""

# to run these tests: python -m unittest test_job_model.py


import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, Job, Location, Category, Experiencelevel, Company

# set an environmental variable to use a different database for tests 
# (we need to do this before we import our app, since that will have already
# connected to the database)

os.environ['DATABASE_URL'] = "postgresql:///job_board_test"


# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class JobModelTestCase(TestCase):
    """Test views for jobs."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()

        l = Location(name="Florida")
        ca = Category(name="Engineering")
        co = Company(name="Apple")
        el = Experiencelevel(name="Entry level")

        db.session.add_all([l, ca, co, el])
        db.session.commit()

        j = Job(name="Engineer", 
                description="Description", 
                location_id=1, 
                category_id=1, 
                experience_level_id=1, 
                company_id=1, 
                created_at="Jan 1, 2020", 
                landing_page_url="landingpage.com")
        self.jid = 94566
        j.id = self.jid
        db.session.add(j)
        db.session.commit()

        self.j = Job.query.get(self.jid)

        self.client = app.test_client()

    # def tearDown(self):
    #     res = super().tearDown()
    #     db.session.rollback()
    #     return res

    # def test_message_model(self):
    #     """Does basic model work?"""
        
    #     m = Message(
    #         text="a warble",
    #         user_id=self.uid
    #     )

    #     db.session.add(m)
    #     db.session.commit()

    #     # User should have 1 message
    #     self.assertEqual(len(self.u.messages), 1)
    #     self.assertEqual(self.u.messages[0].text, "a warble")

    # def test_message_likes(self):
    #     m1 = Message(
    #         text="a warble",
    #         user_id=self.uid
    #     )

    #     m2 = Message(
    #         text="a very interesting warble",
    #         user_id=self.uid 
    #     )

    #     u = User.signup("yetanothertest", "t@email.com", "password", None)
    #     uid = 888
    #     u.id = uid
    #     db.session.add_all([m1, m2, u])
    #     db.session.commit()

    #     u.likes.append(m1)

    #     db.session.commit()

    #     l = Likes.query.filter(Likes.user_id == uid).all()
    #     self.assertEqual(len(l), 1)
    #     self.assertEqual(l[0].message_id, m1.id)


        