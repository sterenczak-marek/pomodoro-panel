"""
WSGI config for sever-web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior
# {{ cookiecutter.project_slug }} directory.
# app_path = os.path.dirname(os.path.abspath(__file__)).replace('/config', '')
# sys.path.append(os.path.join(app_path, 'apps'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")


application = get_wsgi_application()
