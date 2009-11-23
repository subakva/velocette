from django.conf import settings
import logging
from logging import handlers

_simple = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
_detailed = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

_console = logging.StreamHandler()
_console.setFormatter(_simple)

# files rotated weekly, keeping 52 weeks of logs
_root_file = handlers.TimedRotatingFileHandler(settings.LOG_ROOT + 'root.log','D',7,52)
_root_file.setFormatter(_detailed)

_sql_file = handlers.TimedRotatingFileHandler(settings.LOG_ROOT + 'sql.log','D',7,52)
_sql_file.setFormatter(_detailed)

# _jobs_file = handlers.TimedRotatingFileHandler(settings.LOG_ROOT + 'jobs.log','D',7,52)
# _jobs_file.setFormatter(_detailed)

# non-root logs inherit the root handlers
root = logging.getLogger()
root.addHandler(_console)

sql = logging.getLogger('rc.sql')
sql.addHandler(_sql_file)

# jobs = logging.getLogger('rc.jobs')
# jobs.addHandler(_jobs_file)

if settings.DEBUG:
    root.setLevel(logging.INFO)
    sql.setLevel(logging.INFO)
    # jobs.setLevel(logging.INFO)
else:
    root.setLevel(logging.WARNING)
    sql.setLevel(logging.WARNING)
    # jobs.setLevel(logging.WARNING)
