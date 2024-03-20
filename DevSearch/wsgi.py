"""
WSGI config for DevSearch project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from waitress import serve

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DevSearch.settings')

# Initialize the Django application
application = get_wsgi_application()

# Serve the application using Waitress
serve(application)

