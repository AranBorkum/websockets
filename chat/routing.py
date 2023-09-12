from django.urls import path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/socket-server/<transaction_id>", ChatConsumer.as_asgi()),
]
