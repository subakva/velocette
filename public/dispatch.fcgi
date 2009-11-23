#!/home/wadsbone/lib/bin/python
import sys
sys.path += ['/home/wadsbone/sites/']
sys.path += ['/home/wadsbone/sites/velocette/lib/']
from fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'velocette.settings'
WSGIServer(WSGIHandler()).run()

