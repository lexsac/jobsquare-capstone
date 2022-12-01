"""Seed file to make sample data for db."""

from models import User, Job, UserJob, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Create sample users and jobs
u1 = User(first_name="Lexsa", 
            last_name="Campbell", 
            email="lexsa1234@aol.com", 
            username="lexsa1234",
            password="mia1234",
            location="New York, NY",
            category="Software Engineering",
            experience_level="Entry Level",
            company="Google"
)
u2 = User(first_name="Alex", 
            last_name="Saralegui", 
            email="alex1234@aol.com", 
            username="alex1234",
            password="dot1234",
            location="New York, NY",
            category="Product Strategy",
            experience_level="Mid Level",
            company="Comcast"
)
j1 = Job(name="Software Engineer",
            description="You will be a software engineer in this role.",
            location="New York, NY",
            category="Software Engineering",
            experience_level="Entry Level",
            company="Google",
            landing_page_url="www.google.com" 
)
j2 = Job(name="Product Strategist",
            description="You will be a product strategist in this role.",
            location="New York, NY",
            category="Product Strategy",
            experience_level="Mid Level",
            company="Comcast",
            landing_page_url="www.comcast.com" 
)
uj1 = UserJob(user_id=1, job_id=1)
uj2 = UserJob(user_id=2, job_id=2)

db.session.add(u1)
db.session.add(u2)
db.session.add(j1)
db.session.add(j2)
db.session.commit()

db.session.add(uj1)
db.session.add(uj2)
db.session.commit()