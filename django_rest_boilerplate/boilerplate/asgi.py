"""
ASGI config for boilerplate project.

It exposes ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/

"""

import os

from django.core.asgi import get_asgi_application
from django.core.handlers.asgi import ASGIHandler

os.environ.setdefault(
    key="DJANGO_SETTINGS_MODULE", value="boilerplate.settings"
)

application: ASGIHandler = get_asgi_application()
