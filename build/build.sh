#!/bin/bash

cd /vagrant/webapps/geonaut_venv/geonaut
pwd
echo "Git pull"
git pull
echo "activate venv"
. /vagrant/webapps/geonaut_venv/bin/activate
cd /vagrant/webapps/geonaut_venv/geonaut/geonaut
pwd
echo "running makemigrations"
python /vagrant/webapps/geonaut_venv/geonaut/manage.py makemigrations
echo "running migrate"
python /vagrant/webapps/geonaut_venv/geonaut/manage.py migrate
echo "running collectstatic"
python /vagrant/webapps/geonaut_venv/geonaut/manage.py collectstatic --no-input
echo "deactivate"
deactivate