# Flyblog

A simple blog created using django.

## Setup Instructions

python 3.4, pip 1.5.6 and postgreSQL 9.3.16 were used to create this project

### Install Requirements 

```
pip install -r /path/to/requirements.txt
```

### Setup Database

These are the instructions for ubuntu:

```
sudo su - postgres
createdb flyblog
createuser -P flyblog
P: flyblog
psql
ALTER ROLE flyblog CREATEDB;
```


### Django Commands

```
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```
