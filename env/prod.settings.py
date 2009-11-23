DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_ID = 2

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'velocette'
DATABASE_USER = 'velocette'
DATABASE_PASSWORD = '' # see _secrets.py
DATABASE_HOST = 'mysql.subakva.com'
DATABASE_PORT = ''

SERVER_EMAIL = 'noreply@velocette.subakva.com'
DEFAULT_FROM_EMAIL = 'noreply@velocette.subakva.com'
EMAIL_SUBJECT_PREFIX = '[Velocette] '

MEDIA_ROOT = '/home/wadsbone/sites/velocette/static/'
MEDIA_URL = 'http://media.velocette.subakva.com/'
ADMIN_MEDIA_PREFIX = 'http://media.velocette.subakva.com/admin/'

TEMPLATE_DIRS = (
    '/home/wadsbone/sites/velocette/templates/',
)
FIXTURE_DIRS = (
    '/home/wadsbone/sites/velocette/fixtures/',
)

LOG_ROOT = '/home/wadsbone/sites/velocette/logs/'
LOG_SQL = False
LOG_SQL_TO_FILE = False
LOG_SQL_TO_RESPONSE = False

SERVE_STATIC = False
SEND_BROKEN_LINK_EMAILS = True
TEMPLATE_STRING_IF_INVALID = ''
