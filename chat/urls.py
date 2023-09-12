from django.urls import path

from chat.views import chat_window

urlpatterns = [
    path("chat/<transaction_id>/", chat_window),
]
