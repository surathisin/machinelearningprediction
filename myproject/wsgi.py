import os
import sys
from django.core.wsgi import get_wsgi_application

# add your project directory to the sys.path
project_home = '/home/surathisin/MachineLearningPredictionBoard'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'MachineLearningPredictionBoard.settings'

application = get_wsgi_application()

