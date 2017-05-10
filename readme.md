Source Code for Geonaut.co.uk
=============================

This is the source code for my personal portolio site, written in Python. It is relatively simple and lightweight, and makes use of the Django framework and Wagtail CMS for managing content. 

The site also uses:

  * Bootstrap v3
  * JavaScript incl. JQuery
  * Taggit for tags
  * Formspree as a lightweight SMTP relay
  * Django Bootstrap Pagination

Setup a local instance on a Mac
===============================

Requirements: Python, Pip, Virtualenv

1. Create a virtualenv folder on your computer (eg `virtualenv geonaut_venv`)
1. Change into the directory (`cd geonaut_venv`)
1. Download / clone this repo to your virtual env (eg 'git clone https://github.com/geonaut/geonaut-portfolio.git geonaut')
1. Activate the venv (`source bin/activate`)
1. Change into the project directory (`cd geonaut`)
1. Install the requirements (`pip install -r requirements.txt`)
1. Copy settings/local.py.sample to settings/local.py
1. Uncomment the secret key line, and make your own secret key (change / add random characters)
1. Uncomment the Databases snippet (the SQLite one) to base.py
1. Run the development server (`python manage.py runserver` from whichever folder manage.py is in)


To Do List
==========

1. Move homepage copy into CMS
1. Dynamically fetch categories to create filter switches
1. Find a more reliable way to display PDFs
1. Sort script blocking on above-fold content
1. Set on_delete values for on_delete action
1. Add a sitemap
1. Update to Python 3