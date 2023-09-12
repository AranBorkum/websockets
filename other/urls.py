from django.urls import path

from other.views import ButtonCallView

urlpatterns = [
    path("button-call/", ButtonCallView.as_view()),
]
