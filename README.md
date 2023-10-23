# TaskProject
A todo management web application with REST API using django

## Run Webserver
git clone https://github.com/gravityfargo/TaskProject.git && cd TaskProject
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations tasks
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py loaddata sample.json
python3 manage.py runserver


## File Structure
- **TaskProject/**
    - container for the project
- **TaskProject/TaskProject/**
    - "Project" a collection of apps
- **TaskProject/tasks/**
    - "App" a module that can be resued in other projects
- **TaskProject/__init__.py**
    - indicates to the python interpreter that the root folder contains a package
- **TaskProject/urls.py**
    - table of contents for the urls of apps
- **TaskProject/asgi.py**
    - webserver entry point
- **TaskProject/wsgi.py**
    - webserver entry point



