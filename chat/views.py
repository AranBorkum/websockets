from pprint import pprint

from django.core.handlers.asgi import ASGIRequest
from django.shortcuts import render


# Create your views here.
def chat_window(request: ASGIRequest, transaction_id):
    pprint(request.scope)
    response = render(request, "chat.html", {"transaction_id": transaction_id})
    return response
