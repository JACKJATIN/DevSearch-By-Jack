"""
ASGI config for DevSearch project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from daphne.server import Server

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DevSearch.settings')

django_asgi_application = get_asgi_application()

if __name__ == "__main__":
    server = Server(django_asgi_application)
    server.run()
