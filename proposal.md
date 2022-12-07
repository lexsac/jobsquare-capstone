# Capstone Project 1: Job Board App

### Project Proposal

## Overview
A job board app that will allow users to search for and save job postings to their personal profile. The job postings will come from The Muse API(https://www.themuse.com/developers/api/v2?ref=apilist.fun).

## Goals
1. Allow users to create a profile (username and password), as well as set preferences for job category, experience level, location, and company. (Note: Setting these preferences will be required in the initial app).

2. After setting preferences, users will see a list of job postings that match their preference criteria. Users can edit their preferences on their profile page, and they can also 'like' job postings, which will save them to their profile. Users can similarly 'unlike' job postings to remove them from their 'liked' jobs list.

3. [stretch goal] If a user downvotes a job posting, that posting will no longer serve in their search results.

4. [stretch goal] Users can search for job posting by keyword.

5. [stretch goal] Include US-only jobs.

6. [stretch goal] Rank jobs by Newest 

## User Demographics
Users of this site will be job-searching individuals located either in the US or internationally (since job postings included in the initial span all locations) who typically rely on searching job boards for open job postings. Job postings included in this app range from entry level to senior level.

## Data
I will using the The Muse API (https://www.themuse.com/developers/api/v2?ref=apilist.fun), which lists job postings with attributes for company, job category, experience level, and location. It also contains date posted (which I can potentially use to sort job posting search results by 'Newest').

The API docs also mention that I am able to get 'a list of jobs, intelligently sorted by a number of factors, such as trendiness, uniqueness, newness, etc.' I need to research this point further.

## Approach
### Database Schema (This is still in-progress, need to add crow's feet notation)
alt text

### Potential API Complications
1. Location - I am concerned that this API has location as a data attribute yet lists US (city, state) and non-US (city, country) in the same format. For example, 'New York, NY' and 'London, England' are both used as locations for job postings. This will make filtering to US-only jobs (or job postings in English) more difficult.

2. Job description - This API has HTML stored as job description data, and I am not sure how to populate this text with proper formatting. If I use regex expressions to remove HMTL tags, how will I format description text properly?

3. Misc - As mentioned above, this API states that I am able to fetch jobs by 'a number of factors, such as trendiness, uniqueness, newness, etc.' I need to understand how this sorting works, as I want to provide the most relevant job postings for users and may be able to include this data in sorting as a stretch goal.

### Sensitive Information
User passwords will need to be stored securely, so I will be using bcrypt. 

### App Functionality
Users will be able to:

Create a profile (with first name, last name, email, username, and password). They will also be able to indicate preferences for location, experience level, and job category. 

View jobs that match their criteria, and click to Apply (where they'll be taken to the original job posting on The Muse in a new browser window) or 'like' the job posting to save to their profile.

View 'liked' jobs, unlike any jobs currently in their 'liked' jobs list, and update job preferences in their profile.

### User Flow
Users who are not logged in will see the anonymous user homepage, which will urge them to create an account. 

After creating an account, a signed in user will be able to browse their personalized list of postings and 'like' any posting to save it to their profile.

Each job posting will link to a job details page (with more information about that posting) as well as link to the job posting on The Muse. If a user clicks 'Apply', the app will open a new browser window with that original job posting URL.

If users navigate to their liked jobs page, they will see the list of favorited job postings. They can 'unlike' a job posting at any time to remove the job from their list.

If they navigate to their profile page, they will be able to update their password and preferences (job category, experience level, and location).

Finally, users will be able to logout or delete their account if needed.