DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_ID = 3

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'subakva_velo'
DATABASE_USER = 'subakva_velo'
DATABASE_PASSWORD = '' # see _secrets.py
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'subakva'
EMAIL_HOST_PASSWORD = '' # see _secrets.py
SERVER_EMAIL = 'noreply@subakva.webfactional.com'
DEFAULT_FROM_EMAIL = 'noreply@subakva.webfactional.com'
EMAIL_SUBJECT_PREFIX = '[Velocette] '

MEDIA_ROOT = '/home/subakva/webapps/velo_web/velocette/static/'
MEDIA_URL = 'http://media.subakva.webfactional.com/'
ADMIN_MEDIA_PREFIX = 'http://media.velocette.subakva.com/admin/'

TEMPLATE_DIRS = (
    '/home/subakva/webapps/velo_web/velocette/templates/',
)
FIXTURE_DIRS = (
    '/home/subakva/webapps/velo_web/velocette/fixtures/',
)

USE_SSL = True

LOG_ROOT = '/home/subakva/webapps/velo_web/velocette/logs/'
LOG_SQL = False
LOG_SQL_TO_FILE = False
LOG_SQL_TO_RESPONSE = False

SERVE_STATIC = False
SEND_BROKEN_LINK_EMAILS = True
TEMPLATE_STRING_IF_INVALID = ''
