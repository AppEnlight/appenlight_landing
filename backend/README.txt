appenlight_landing README
==================

Getting Started
---------------

- cd <directory containing this file>
- $VENV/bin/python setup.py develop
- $VENV/bin/initialize_appenlight_landing_db development.ini
- $VENV/bin/pserve development.ini



Getting Started for Dummies [by Lisa]
-------------------------------------

Prerequisites: virtualenv

The website runs inside of virtualenv. The application itself
is inside of the /python/ folder; use development.ini to utilise
debugging parameters.

Run these commands:
$ virtualenv env
$ source env/bin/activate
$ cd python
$ python setup.py develop
$ initialize_appenlight_landing_db development.ini
$ pserve development.ini
You should now see the website at the address listed at the bottom of the output.


After setup, to build static site copy the make_static.sh from the repo,
alter the paths and run it to build html and copy to right location
