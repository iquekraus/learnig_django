# learning_django

### Instaling host dependencies
    $ sudo apt-get install python3
    

### New project
    $ python3 -m venv venv
    $ . venv/bin/activate
    (venv) pip install django
    (venv) django-admin startproject pontos_turisticos .
    (venv) pip install djangorestframework
    
    (venv) python manage.py createsuperuser
    
### Creating an App
    (venv) python manage.py startapp core
    
### Installing Pillow
    (venv) pip install Pillow
    
### Installing Django-Filter
[Tutorial here](https://www.django-rest-framework.org/api-guide/filtering/)
    
    (venv) pip install django-filter
    
### Deploying to Heroku CLI

[Tutorial here](https://devcenter.heroku.com/articles/heroku-cli)

[And here](https://devcenter.heroku.com/articles/heroku-cli)
    
    $ sudo snap install --classic heroku
    $ heroku login
    
    (venv) pip install python-decouple
    (venv) pip install dj-database-url
    (venv) pip install dj-static
    
### Creating requirements file

    (venv) pip freeze > requirements-dev.txt
