DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'velocette_dev'
DATABASE_USER = 'velocette'
DATABASE_PASSWORD = 'velocette'
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''

EMAIL_HOST = 'smtp.comcast.net'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = 'noreply@localhost'
DEFAULT_FROM_EMAIL = 'noreply@localhost'
EMAIL_SUBJECT_PREFIX = '[Velocette @tuber] '

MEDIA_ROOT = '/Users/jason/Code/subakva/velocette/static/'
MEDIA_URL = 'http://localhost:8000/static/'
ADMIN_MEDIA_PREFIX = 'http://localhost:8000/static/admin/'

TEMPLATE_DIRS = (
    '/Users/jason/Code/subakva/velocette/templates/',
)
FIXTURE_DIRS = (
    '/Users/jason/Code/subakva/velocette/fixtures/',
)

LOG_ROOT = '/Users/jason/Code/subakva/velocette/logs/'
LOG_SQL = False
LOG_SQL_TO_FILE = True
LOG_SQL_TO_RESPONSE = False

SERVE_STATIC = True
SEND_BROKEN_LINK_EMAILS = False
TEMPLATE_STRING_IF_INVALID = ''

#Dummy mail handler that prints email messages to the console
from django.core import mail

class TestSMTP(object):
    def sendmail(self, sender, recipients, message):
        print('--- SENT EMAIL ---\n%s' % str(message))

class TestSMTPConnection(mail.SMTPConnection):
    def open(self):
        self.connection = TestSMTP()
        return True
    def close(self): self.connection = None

    @staticmethod
    def install():
        mail.SMTPConnection = TestSMTPConnection

TestSMTPConnection.install()
