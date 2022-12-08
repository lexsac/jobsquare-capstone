"""Seed file to make sample data for db."""

from models import User, Job, UserJob, db, Location, Category, Experiencelevel, Company
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
            with app.app_context():
                j = Job(name=job_info['name'],
                    description=job_info['contents'],
                    location=job_info['locations'][0]['name'],
                    # category=job_info['categories'][0]['name'],
                    category = "filler text",
                    experience_level=job_info['levels'][0]['name'],
                    company=job_info['company']['name'],
                    landing_page_url=job_info['refs']['landing_page'] 
                )
                if (Location.query.filter_by(name=job_info['locations'][0]['name']).first() == None):
                    l = Location(name=job_info['locations'][0]['name'])
                    db.session.add(l)
                if (Category.query.filter_by(name=job_info['locations'][0]['name']).first() == None):
                    ca = Category(name=job_info['locations'][0]['name'])
                    db.session.add(ca)
                if (Experiencelevel.query.filter_by(name=job_info['levels'][0]['name']).first() == None):
                    e = Experiencelevel(name=job_info['levels'][0]['name'])
                    db.session.add(e)
                if (Company.query.filter_by(name=job_info['company']['name']).first() == None):
                    co = Company(name=job_info['company']['name'])
                    db.session.add(co)
                db.session.add(j)
                db.session.commit()

get_jobs(1,20)

# def get_jobs(start_page_num, end_page_num):

#     for page_num in range(start_page_num, end_page_num):
#         response = requests.get(f"{API_BASE_URL}?page={page_num}", params={"key": API_SECRET_KEY}).json()
        
#         for job_info in response['results']:
#             job_list.append([job_info['name'], job_info['contents'], job_info['locations'][0]['name'], 'filler for category data', job_info['levels'][0]['name'], job_info['company']['name'], job_info['refs']['landing_page']])

# num_of_jobs = len(job_list)

# for num in range(num_of_jobs):
#     with app.app_context(): 
#         if (Location.query.filter_by(name=job_list[num][2]).first() == None):
#             l = Location(name=job_list[num][2])
#         if (Category.query.filter_by(name=job_list[num][3]).first() == None):
#             ca = Category(name=job_list[num][3])
#         if (Experiencelevel.query.filter_by(name=job_list[num][4]).first() == None):
#             e = Experiencelevel(name=job_list[num][4])
#         if (Company.query.filter_by(name=job_list[num][5]).first() == None):
#             co = Company(name=job_list[num][5])
#         db.session.add(l)
#         # db.session.add(ca)
#         db.session.add(e)
#         db.session.add(co)
#         db.session.commit()


# for num in range(num_of_jobs):
#     j = Job(name=job_list[num][0],
#             description=job_list[num][1],
#             location=job_list[num][2],
#             category='filler text',
#             experience_level=job_list[num][4],
#             company=job_list[num][5],
#             landing_page_url=job_list[num][6] 
#             )
#     with app.app_context():     
#         db.session.add(j)
#         db.session.commit()





