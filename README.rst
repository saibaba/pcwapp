=========================================================
Template application to build django based web app on GAE
=========================================================

Running
=======

Running template app locally
----------------------------

Use th following steps to run the restfulapi application locally:

1) Get the code from github

::

   git clone https://github.com/saibaba/pcwapp.git


2) Change to the application directory

::

  cd pcwapp


3) Launch GAE development, for example

::

  dev_appserver.py -a 127.0.0.1 -p 9080 -d  .

4) Point browser at: http://localhost:9080/helloworld/


To deploy your own instance of the app to Google App Engine
-----------------------------------------------------------

1. Register your own application ID on the App Engine admin site.
2. Edit app.yaml to use this app ID instead of 'pcwapp'.
3. Upload using (run from the parent directory where you cloned this git repo into)

::

  appcfg.py update pcwapp


Developing
----------

See the sample django project in helloworld folder. Copy it and modify as needed.

=========
Referenes
=========

1) http://code.google.com/p/rietveld/source/browse/settings.py
2) http://code.google.com/p/rietveld/
