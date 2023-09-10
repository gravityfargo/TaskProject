A todo management web application with REST api using django

python manage.py makemigrations tasks
python manage.py migrate

python manage.py createsuperuser

-   **TaskProject/**
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

