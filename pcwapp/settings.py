import os

from google.appengine.api import app_identity

dirname = os.path.dirname(globals()["__file__"])

APPEND_SLASH = False

DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')

INSTALLED_APPS = (
    'helloworld',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'pcwapp.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
    os.path.join(dirname, '../helloworld/templates'),
    os.path.join(dirname, '../templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',          
)

FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
)

FILE_UPLOAD_MAX_MEMORY_SIZE = 1048576  # 1 MB

MEDIA_URL = '/static/'

appid = app_identity.get_application_id()

