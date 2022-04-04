# Prerequisites 
This app is build using FastApi framework. And for database it uses Postgres.
The database is hosted on a remote server(https://api.elephantsql.com/).


# Steps to run note-api
1. Make sure you have Docker installed on your machine.
2. run command `docker-compose build`
3. run command `docker-compose up`

# Development Server
Navigate to `http://localhost:8000`

# Api Docs
To see the list of available api's you can navigate to `http://localhost:8000/docs`

![Screen Shot 2565-04-04 at 04 19 09](https://user-images.githubusercontent.com/91866412/161449092-41207b7f-7980-46d4-9e63-8397857d877a.png)

# Tests
To run test run this command `pytest tests/test_api.py -s`


# Table Schema
## Authors
![Screen Shot 2565-04-04 at 04 06 26](https://user-images.githubusercontent.com/91866412/161448707-5ee693cc-1786-4d4c-8e4a-61518380bbde.png)

## Blogs
![Screen Shot 2565-04-04 at 04 07 58](https://user-images.githubusercontent.com/91866412/161448747-da8df8d4-dcf8-47a6-96e4-26436e378ce9.png)

## Categories
![Screen Shot 2565-04-04 at 04 08 55](https://user-images.githubusercontent.com/91866412/161448778-d816762b-c02a-44c4-ad39-db4e2155ae00.png)
