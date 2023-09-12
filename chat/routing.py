from django.urls import re_path, path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/socket-server/<transaction_id>", ChatConsumer.as_asgi()),
]
