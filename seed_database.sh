#!/bin/bash

rm db.sqlite3
rm -rf ./magicapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations magicapi
python3 manage.py migrate magicapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata participants
python3 manage.py loaddata services
python3 manage.py loaddata magicianservices
