# cowrywise_application
Stack Used
Django
django-rest-framework 

## create virtual env
>>> virtualenv -p python3 venv

## activate virtualenv
>>> source ./venv/bin/activate
## install requirements
>>> pip install -r requirements.txt

## make migrations to sqlite db
>>> python manage.py makemigrations

## migrate the database
>>> python manage.py migrate

## run the server
>>> python manage.py runserver 0.0.0.0:8004

## Go to Api Endpoint on browser
http://127.0.0.1:8004/perform-magic/
