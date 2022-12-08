"""Seed file to make sample data for db."""

from models import db, Job, Location, Category, Experiencelevel, Company
from app import app
import requests
from key import API_SECRET_KEY

API_BASE_URL = "https://www.themuse.com/api/public/jobs"


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
                        description = "filler text",
                        # description=job_info['contents'],
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

# locations = Location.query.all()
# locations_list = []
# for location in locations:
#     locations_list.append((location.id, location.name))

# def get_jobs(start_page_num, end_page_num):

#     for page_num in range(start_page_num, end_page_num):
#         resp = requests.get(f"{API_BASE_URL}?page={page_num}", params={"key": API_SECRET_KEY}).json()

#     return resp['results']


# response = get_jobs(1,20)

# for job_info in response:
#     with app.app_context():
#         j = Job(name=job_info['name'],
#             description=job_info['contents'],
#             location=job_info['locations'][0]['name'],
#             # category=job_info['categories'][0]['name'],
#             category = "filler text",
#             experience_level=job_info['levels'][0]['name'],
#             company=job_info['company']['name'],
#             landing_page_url=job_info['refs']['landing_page'] 
#             )
#         if (Location.query.filter_by(name=job_info['locations'][0]['name']).first() == None):
#             l = Location(name=job_info['locations'][0]['name'])
#             db.session.add(l)
#         if (Category.query.filter_by(name=job_info['locations'][0]['name']).first() == None):
#             ca = Category(name=job_info['locations'][0]['name'])
#             db.session.add(ca)
#         if (Experiencelevel.query.filter_by(name=job_info['levels'][0]['name']).first() == None):
#             e = Experiencelevel(name=job_info['levels'][0]['name'])
#             db.session.add(e)
#         if (Company.query.filter_by(name=job_info['company']['name']).first() == None):
#             co = Company(name=job_info['company']['name'])
#             db.session.add(co)
        
#         db.session.add(j)
#         db.session.commit()
