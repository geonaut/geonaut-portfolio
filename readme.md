Source Code for Geonaut.co.uk
=============================

This is the source code for my [personal portolio site](https://geonaut.co.uk), written in Python. It is relatively simple and lightweight, and makes use of the Django framework and Wagtail CMS for managing content. 

The site also uses:

  * Bootstrap v3
  * Formspree as a lightweight SMTP relay (contact page)
  * JavaScript incl. JQuery (blog)
  * Taggit for tags (blog)
  * Django Bootstrap Pagination (blog)

Quickstart for Mac
==================

Requirements: Python 2.7, Pip, Virtualenv

1. Using terminal, create a folder somewhere (eg `mkdir mysite`)
1. Move into that folder
1. Create a virtualenv folder (e.g. `virtualenv venv`)
1. Download / clone this repo to a folder inside `mysite` (e.g. `git clone https://github.com/geonaut/geonaut-portfolio.git geonaut`)
1. Activate the venv (`source venv/bin/activate`)
1. Change into the project directory (`cd geonaut`)
1. Install the requirements (`pip install -r requirements.txt`)
1. Switch to your IDE. Add the geonaut folder, to see the files.
1. Copy geonaut/geonaut/settings/local.py.sample to /settings/local.py
1. Uncomment the `DATABASES = ...` snippet (the SQLite one) in `base.py`
1. Option 1: To use a pre-populated database
    -  Copy the quickstart/db.sqlite3 to the folder above /quickstart
    -  Copy the quickstart/media folder to the folder above /quickstart
    -  The username is `admin` and password is `password`
1. Option 2: To create your own empty database
    -  Create the database with `python manage.py migrate`
    -  Create a superuser with `python manage.py createsuperuser`
    -  The site will be empty, except for the static homepage
1. Run the development server (`python manage.py runserver` from whichever folder manage.py is in)
1. Access the site at http://127.0.0.1:800 and http://127.0.0.1/admin

If/when you decide to make your site live, you will need to do various other things, such as:

1. Make your own secret key (change / add random characters)
1. Move to PostgreSQL
1. Move to a production webserver (Nginx / Gunicorn)
1. Delete the default superuser, and create your own


To Do List
==========

1. Dynamically fetch categories to create filter switches
1. Find a more reliable way to display PDFs
1. Sort script blocking on above-fold content
1. Add a sitemap
1. Update to Python 3