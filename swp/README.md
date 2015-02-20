csportal
========

The CS Portal is a website where Carolina CS students can collaborate in projects, share important job hunting information and look for internships and full time job opportunities.

To download the site simply clone this repository and install the third party dependencies. 

1) First, install pip for python, a tool for installing python packages
```
python get-pip.py
```
2) Then install the external libraries used in this project
```
pip install beautifulsoup
pip install simplejson
pip install django-wysiwyg
pip install django-registration
```
3) To run the local development server, navigate to the folder ```csportal``` where the code resides and do:

```
python manage.py runserver
```

4) The site should now be running on localhost

Possible additions
=======
- Not having to edit password everytime a password protected post is edited
- Running the database deletion command with the cron manager
- Migrating to PostgreSQL
