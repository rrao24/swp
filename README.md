csportal
========

The CS Portal is a website where Carolina CS students can collaborate in projects, share important job hunting information and look for internships and full time job opportunities.

To download the site simply clone this repository and install the third party dependencies. 

1) First, install pip for python, a tool for installing python packages
```
python get-pip.py
```
2) Then install the external libraries used in this project as specified by the requirements text file
```
pip install -r requirements.txt
```
3) To host on Apache, make the Apache system user (var-www or the like) the owner of necessary files (everything in the swp directory should be sufficient). Also, make sure Apache is set up to run with wsgi and points to a wsgi entry point (in our case, index.wsgi).
