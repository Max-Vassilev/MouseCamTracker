from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/mouse_tracking/$', consumers.MouseConsumer.as_asgi()),
    re_path(r'ws/mouse_click/$', consumers.MouseClickConsumer.as_asgi()), 
]
