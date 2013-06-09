import os
import sys
sys.path.append('/home/laboratorio')
os.environ['DJANGO_SETTINGS_MODULE'] = 'labs.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/laboratorio/labs'
if path not in sys.path:
    sys.path.append(path)

