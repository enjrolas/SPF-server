import os
import sys

path = '/home/japhy/solarPocketFactory/'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'solarPocketFactory.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()