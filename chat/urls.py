from django.urls import path

from chat.views import (
    chat_window,
    transactions_window,
    ListTransactionsView,
    TransactionInformationView,
)

urlpatterns = [
    path("chat/<transaction_id>/", chat_window),
    path("transactions/", transactions_window),
    path("api/list-transactions/", ListTransactionsView.as_view()),
    path("api/get-transaction-info/", TransactionInformationView.as_view()),
]
