import json
from pprint import pprint

from django.core.handlers.asgi import ASGIRequest
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from chat.models import TransactionModel


def chat_window(request: ASGIRequest, transaction_id):
    pprint(request.scope)
    response = render(request, "chat.html", {"transaction_id": transaction_id})
    return response


def transactions_window(request: ASGIRequest):
    response = render(request, "transactions.html")
    return response


class ListTransactionsView(APIView):
    def get(self, request: HttpRequest):
        transactions = TransactionModel.objects.all()
        data = [str(tx.id) for tx in transactions]
        return Response(
            data=json.dumps({"transaction_ids": data}),
            status=status.HTTP_200_OK,
        )


class TransactionInformationView(APIView):
    def get(self, request: HttpRequest):
        transaction = TransactionModel.objects.get(id=request.META["QUERY_STRING"])
        data = transaction.information
        return Response(data=json.dumps(data), status=status.HTTP_200_OK)

    def put(self, request: Request):
        transaction_id = request.data.get("id")
        information = request.data.get("information")
        transaction_model = TransactionModel.objects.get(id=transaction_id)
        transaction_model.information = information
        transaction_model.save()
        return Response(status=status.HTTP_200_OK)
