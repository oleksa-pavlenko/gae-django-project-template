import os

from django.core.wsgi import get_wsgi_application
from djangae.wsgi import DjangaeApplication

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
application = DjangaeApplication(get_wsgi_application())