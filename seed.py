"""Seed file to make sample data for db."""

from models import User, Job, UserJob, db
from app import app
import requests
from key import API_SECRET_KEY

API_BASE_URL = "https://www.themuse.com/api/public/jobs"
job_list= []

# Create all tables
with app.app_context():     
    db.drop_all()
    db.create_all()


def get_jobs(start_page_num, end_page_num):

    for page_num in range(start_page_num, end_page_num):
        response = requests.get(f"{API_BASE_URL}?page={page_num}", params={"key": API_SECRET_KEY}).json()
        
        for job_info in response['results']:
            job_list.append([job_info['name'], job_info['contents'], job_info['locations'][0]['name'], job_info['categories'][0]['name'], job_info['levels'][0]['name'], job_info['company']['name'], job_info['refs']['landing_page']])

get_jobs(1,10)
num_of_jobs = len(job_list)

for num in range(num_of_jobs):
    j = Job(name=job_list[num][0],
            description=job_list[num][1],
            location=job_list[num][2],
            category=job_list[num][3],
            experience_level=job_list[num][4],
            company=job_list[num][5],
            landing_page_url=job_list[num][6] 
            )
    with app.app_context():     
        db.session.add(j)
        db.session.commit()

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


uj1 = UserJob(user_id=1, job_id=1)
uj2 = UserJob(user_id=2, job_id=2)

with app.app_context():     
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    db.session.add(uj1)
    db.session.add(uj2)
    db.session.commit()
