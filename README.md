# Django YouTube API Project

This project is a Django application that fetches the latest videos from YouTube for a predefined search query and stores the video data in a PostgreSQL database.

## Features

- Fetches latest videos from YouTube API at regular intervals using Celery and Redis.
- Stores video data in a PostgreSQL database.
- Provides a GET API that returns the stored video data in a paginated response, sorted in descending order of published datetime.

## Installation

- Clone this repository.
- Install the required packages using pip:

## shell
pip install -r requirements.txt

## Set up the PostgreSQL database:

- sudo -u postgres psql
- CREATE DATABASE your_database_name;
- CREATE USER your_username WITH PASSWORD 'your_password';
- GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;
- \q

## Update the DATABASES setting in settings.py with your PostgreSQL database details.

- Run migrations to create the database schema:
- python manage.py makemigrations
- python manage.py migrate
- Run the  django server
- python manage.py runserver

## In a separate terminal window, run the Celery worker:

- celery -A your_project_name worker --loglevel=info
## In another terminal window, run the Celery beat scheduler:
- celery -A your_project_name beat --loglevel=info

You can access the GET API at http://localhost:8000/api/videos/.

