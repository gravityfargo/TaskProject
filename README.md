# TaskProject
A todo management web application with REST API using django

## Run Webserver
***System Prerequisites***: python, pip, venv

`git clone https://github.com/gravityfargo/TaskProject.git && cd TaskProject`

`python3 -m venv .venv`

`source .venv/bin/activate`

`python3 -m pip install -r requirements.txt`

`python3 manage.py makemigrations tasks`

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

`python3 manage.py loaddata sample.json`

`python3 manage.py runserver`

Navigate to [http://127.0.0.1:42069/](http://127.0.0.1:42069/)


## File Structure
- **TaskProject/**
    - container for the project
- **TaskProject/TaskProject/**
    - Defines the python project, "a collection of apps"
- **TaskProject/tasks/**
    - "App" a submodule of the project
- **TaskProject/templates/**
    - holds the html templates used globally across the project
- **TaskProject/__init__.py**
    - indicates to the python interpreter that the root folder contains a package
- **TaskProject/urls.py**
    - table of contents for the urls of apps
- **TaskProject/asgi.py**
    - webserver entry point
- **TaskProject/wsgi.py**
    - webserver entry point


## Database (Model) Changes
- if more than one database colum is changed, you must migrate from scratch, so remove the "migrations" folder before running make migrations and migrate
- whenever changes are made to models.py, run makemigrations

## Extending the base.html template for new apps
```
{% extends "base.html" %}
{% block title %}NEW_APP_NAME{% endblock title %}
{% block activelinkNEW_APP_NAME %}active{% endblock activelinkNEW_APP_NAME %}
{% block content %}
{% block NEW_APP_NAMEcontent %}
{% endblock NEW_APP_NAMEcontent %}
{% endblock content %}
```
**extends**: imports that html file

**title:** sets the site tag which will end up being "TaskProject - NEW_APP_NAME"

**activelinkNEW_APP_NAME:** adds the "active" css to the link in the nave bar. Note, you need to add a new navitem as well.

**block content:** everything in this block will be put inside the <body> tag in the parent base.html file

**block NEW_APP_NAMEcontent:** this creates a sub block inside content specifically for the the app

## Planned
- django-bootstrap-modal-forms
- django-rest-api
- calendar app
    - nextcloud [caldav integration](https://github.com/python-caldav/caldav)
- notes app
- dedicated desktop (electron app?)
- dedicated android app