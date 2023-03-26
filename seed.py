"""Seed file to make sample data for db."""

import os

from models import db, Job, Location, Category, Experiencelevel, Company, User, UserJob
from app import app
import requests

API_BASE_URL = "https://www.themuse.com/api/public"
SECRET_KEY = os.environ.get('SECRET_KEY')

# Create all tables
with app.app_context():   
     
    db.drop_all()
    db.create_all()

    def get_jobs(start_page_num, end_page_num):
        for page_num in range(start_page_num, end_page_num):
            response = requests.get(f"{API_BASE_URL}/jobs?page={page_num}", params={"key": SECRET_KEY}).json()
            
            for job_info in response['results']:
                with app.app_context():
                    if (job_info['locations'] and Location.query.filter_by(name=job_info['locations'][0]['name']).first() == None):
                        l = Location(name=job_info['locations'][0]['name'])
                        db.session.add(l)
                        location_id = Location.query.filter_by(name=job_info['locations'][0]['name']).first().id

                    if (job_info['categories'] and Category.query.filter_by(name=job_info['categories'][0]['name']).first() == None):
                        ca = Category(name=job_info['categories'][0]['name'])
                        db.session.add(ca)
                        category_id = Category.query.filter_by(name=job_info['categories'][0]['name']).first().id

                    if (job_info['levels'] and Experiencelevel.query.filter_by(name=job_info['levels'][0]['name']).first() == None):
                        e = Experiencelevel(name=job_info['levels'][0]['name'])
                        db.session.add(e)
                        experience_level_id = Experiencelevel.query.filter_by(name=job_info['levels'][0]['name']).first().id

                    if (job_info['company'] and Company.query.filter_by(name=job_info['company']['name']).first() == None):
                        co = Company(name=job_info['company']['name'])
                        db.session.add(co)
                        company_id = Company.query.filter_by(name=job_info['company']['name']).first().id

                    j = Job(name=job_info['name'],
                        description=job_info['contents'] if job_info['contents'] else None,
                        location_id=location_id if job_info['locations'] else None,
                        category_id=category_id if job_info['categories'] else None,
                        experience_level_id=experience_level_id,
                        company_id=company_id if job_info['company'] else None,
                        created_at=job_info['publication_date'],
                        landing_page_url=job_info['refs']['landing_page'] 
                    )
                    db.session.add(j)
                    db.session.commit()

    def add_logo_to_companies(start_page_num, end_page_num):
        for page_num in range(start_page_num, end_page_num):
            response = requests.get(f"{API_BASE_URL}/companies?page={page_num}", params={"key": SECRET_KEY}).json()

            for company in response['results']:
                with app.app_context():
                    if Company.query.filter_by(name=company['name']).first() == None:
                        co = Company(name=company['name'], logo_img=company['refs']['logo_image'])
                        db.session.add(co)
                        db.session.commit()
                    else: 
                        co = Company.query.filter_by(name=company['name']).first()
                        co.logo_img = company['refs']['logo_image']
                        db.session.add(co)
                        db.session.commit()

    get_jobs(0,99)
    add_logo_to_companies(0,99)