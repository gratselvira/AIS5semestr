"""
WSGI config for iswork project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Этот файл необходим для запуска проекта на сервере. Он содержит конфигурацию WSGI (Web Server Gateway Interface).
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iswork.settings')

application = get_wsgi_application()
