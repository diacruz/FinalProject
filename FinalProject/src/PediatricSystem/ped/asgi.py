"""
ASGI config for ped project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ChannelNameRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from pediatric import consumers

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ped.settings")

ped_asgi_app = get_asgi_application()

# for channels support
application = ProtocolTypeRouter(
    {
        "http": ped_asgi_app,
        "channel": ChannelNameRouter(
            {
                "patient-add": consumers.SimplePatientConsumer.as_asgi(),
            }
        ),
    }
)
