'''
Contains common Django settings for the velocette.example.com project. Enviroment-
specific settings are in the env/ folder. The bin/init.<env-name>.sh script
should copy the appropriate env/<env-name>.py local settings file to
env/_local.py, which is included by this file.

In addition, settings that should not be checked in to version control can
be included in env/_secrets.py This should be used for secret things, like
Paypal credentials and database passwords.
'''

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jason Wadsworth', 'jdwadsworth@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%%yf#d-d87yh#yphn9(1f6+#$=ohe*v4rf+@f6n^cwxa%os()l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    # 'django.middleware.http.ConditionalGetMiddleware'.
    'velocette.middleware.sqllog.SQLLogMiddleware',
    'velocette.middleware.ssl_redirect.SSLRedirect',
    'velocette.middleware.xhr.XHRMiddleware',
    'notifications.NotificationMiddleware',
)

ROOT_URLCONF = 'velocette.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "notifications.notifications"
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.formtools',
    'django.contrib.sessions',
    'django.contrib.sites',
    # plugins
    'compress',
    'django_extensions',
    'dmigrations',
    'timezones',
    # apps
    'velocette.tasks',
    'velocette.accounts',
)

#middleware
USE_ETAGS = True
USE_I18N = False # maybe later

# auth + registration
LOGIN_URL = '/sessions/new/'
LOGIN_REDIRECT_URL = '/tasks/'
AUTH_PROFILE_MODULE = 'accounts.profile'

# ssl
USE_SSL = False

# logging - overridden by env settings
LOG_ROOT = ''
LOG_SQL = False
LOG_SQL_TO_FILE = False
LOG_SQL_TO_RESPONSE = False

# dmigrations
import os
DMIGRATIONS_DIR = os.path.join(os.path.dirname(__file__), 'db/migrations')
DISABLE_SYNCDB =True

# compress
COMPRESS_VERSION = True
COMPRESS_CSS_FILTERS = []
COMPRESS_CSS = {
    'screen': {
        'source_filenames': ['css/boxy.css', 'css/style.css', 'css/iphone.css'],
        'output_filename': 'css/screen.r?.css',
    }
}
COMPRESS_JS_FILTERS = ['compress.filters.jsmin.JSMinFilter']
COMPRESS_JS = {
    'all': {
        'source_filenames': ['js/jquery-1.2.6.js', 'js/jquery.boxy.js', 'js/init.js'],
        'output_filename': 'js/all.r?.js',
    }
}

#imports the environment-specific settings
from env._local import *

#imports the private settings (if they exist)
try:
    from env._secrets import *
except ImportError, e:
    pass # There are no secrets here.

