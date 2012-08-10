import os
import sys
import logging

logging.info('Loading %s, app version = %s', __name__, os.getenv('CURRENT_VERSION_ID'))

import appengine_config

# AppEngine imports.
from google.appengine.ext.webapp import util

# Import webapp.template.  This makes most Django setup issues go away.
from google.appengine.ext.webapp import template


# Import various parts of Django.
import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch.dispatcher
import django.forms


def log_exception(*args, **kwds):
    """Django signal handler to log an exception."""
    cls, err = sys.exc_info()[:2]
    logging.exception('Exception in request: %s: %s', cls.__name__, err)


# Log all exceptions detected by Django.
django.core.signals.got_request_exception.connect(log_exception)

# Unregister Django's default rollback event handler.
django.core.signals.got_request_exception.disconnect( django.db._rollback_on_exception)

# Create a Django application for WSGI.
application = django.core.handlers.wsgi.WSGIHandler()

def real_main():
    """Main program."""
    # Run the WSGI CGI handler with that application.
    util.run_wsgi_app(application)


def profile_main():
    """Main program for profiling."""
    import cProfile
    import pstats
    import StringIO

    prof = cProfile.Profile()
    prof = prof.runctx('real_main()', globals(), locals())
    stream = StringIO.StringIO()
    stats = pstats.Stats(prof, stream=stream)
    # stats.strip_dirs()  # Don't; too many modules are named __init__.py.
    stats.sort_stats('time')  # 'time', 'cumulative' or 'calls'
    stats.print_stats()  # Optional arg: how many to print
    # The rest is optional.
    # stats.print_callees()
    # stats.print_callers()
    print '\n<hr>'
    print '<h1>Profile</h1>'
    print '<pre>'
    print stream.getvalue()[:1000000]
    print '</pre>'

# Set this to profile_main to enable profiling.
main = real_main

if __name__ == '__main__':
    main()
