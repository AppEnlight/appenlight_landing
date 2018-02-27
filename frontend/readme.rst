Javascript frontend for AppEnlight
===================================

To fetch all the requirememts you need to have nodejs and npm installed on
your dev machine, then from `frontend` dir execute::

    npm install
    npm install -g bower
    npm install -g grunt-cli

This will fetch all the required components to build front with grunt.

You may want to adjust the AE_REPO_LOCATION in the location.ini to point to appenlight pyramid application,
by default it is "../rhodecode-appenlight/appenlight".

To build production version (builds both js and css) just run::

    grunt

To work on dev code version (builds js with comments and css) run:

    grunt watch

You generally shouldn't need to run those separately but still:

To work on just Javascript version with comments run:

    grunt watch:dev

To work on just CSS files run:

    grunt watch:css


