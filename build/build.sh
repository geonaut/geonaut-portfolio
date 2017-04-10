#!/bin/bash

cd /vagrant/webapps/geonaut_venv/geonaut
git pull
. /vagrant/webapps/geonaut_venv/bin/activate
cd /vagrant/webapps/geonaut_venv/geonaut/geonaut
python /vagrant/webapps/geonaut_venv/geonaut/manage.py makemigrations
python /vagrant/webapps/geonaut_venv/geonaut/manage.py migrate
python /vagrant/webapps/geonaut_venv/geonaut/manage.py collectstatic --no-input
deactivate