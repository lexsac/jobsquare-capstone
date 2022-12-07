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
I will using the The Muse API(https://www.themuse.com/developers/api/v2?ref=apilist.fun), which lists job postings with attributes for company, job category, experience level, and location. It also contains date posted (which I can potentially use to sort job posting search results by 'Newest').

The API docs also mention that I am able to get 'a list of jobs, intelligently sorted by a number of factors, such as trendiness, uniqueness, newness, etc.' I need to research this point further.

## Approach
### Database Schema (This is still in-progress, need to add crow's feet notation)
alt text

### Potential Complications with API
Making too many requests (the API docs state that unless I register the app, I'm limited to 500 requests per hour).
As mentioned above, this API states that I am able to fetch jobs by 'a number of factors, such as trendiness, uniqueness, newness, etc.' I need to understand how this sorting works, as I want to provide the most relevant job postings for users.
The API docs also state that I need to declare a page number to load - am I able to specify multiple pages?

### Sensitive Information
User passwords, which will need to be secured with bcrypt.

### App Functionality
Users will be able to:

Create a profile (with first name, last name, email, username, and password). They will also be able to indicate preferences for location, experience level, and/or job category. While these preferences are optional, they will filter the available jobs for them so that their job search results are customized to their profile.

Search by keyword for job postings, 'like' job postings (that will then be saved to their profile), and view their list of 'liked' job postings. Users will also be able to 'unlike' jobs to remove them from the list.

### User Flow
Users who are not logged in will see the homepage with job postings listed by 'Newest' as well as the search bar, where they can filter job postings by 'keyword'. These users will not be able to save job postings to their profile.

Users can create an account, and after doing so, will be able to browse their personalized list of postings, search for postings by 'keyword', and 'like' job postings.

If they navigate to their liked jobs page, they will see the list of favorited job postings. Each of these postings will link to a job details page.

If they navigate to their profile page, they will be able to update their password and preferences (job category, experience level, and location).