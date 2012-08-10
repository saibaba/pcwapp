import os
import logging

logging.info('Loading %s from %s', __name__, __file__)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pcwapp.settings'

