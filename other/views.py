import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ButtonCallView(APIView):
    @staticmethod
    def websocket_send(tx_id):
        channel_layer = get_channel_layer()
        print(channel_layer)
        async_to_sync(channel_layer.group_send)(
            tx_id,
            {
                "message": "From button",
                "type": "from_button",
            },
        )

    def post(self, request: Request):
        print("Button pressed")
        data = json.loads(request.body.decode())
        print(data.get("transaction_id"))
        self.websocket_send(str(data.get("transaction_id")))
        return Response(status=status.HTTP_200_OK)