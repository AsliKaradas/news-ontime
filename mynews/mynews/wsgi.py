"""
WSGI config for mynews project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import logging
from django.core.wsgi import get_wsgi_application

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('Starting WSGI application')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mynews.mynews.settings')

try:
    application = get_wsgi_application()
    logger.debug('WSGI application loaded successfully')
except Exception as e:
    logger.error('Failed to load WSGI application', exc_info=e)
    raise

