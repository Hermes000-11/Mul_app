from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/room/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
# basically routing is just urls.py, but for websocket
# the re_path is a regular expression so here what it means:
# r'...' raw string, so '/' isn ot escaping