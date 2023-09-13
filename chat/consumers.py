import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    room_name: str = ""

    async def connect(self):
        transaction_id = str(self.scope["url_route"]["kwargs"]["transaction_id"])
        print(f"connected to {transaction_id}")
        self.room_name = transaction_id
        await self.channel_layer.group_add(
            transaction_id,
            self.channel_name,
        )

        await self.accept()
        await self.send(
            text_data=json.dumps(
                {
                    "message": "Connection Accepted",
                }
            )
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "input_message",
                "message": data.get("message"),
            },
        )

    async def disconnect(self, code):
        await self.send(text_data=json.dumps({"message": "Disconnected"}))
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def input_message(self, event):
        print(event)
        await self.send(text_data=json.dumps({"message": event.get("message")}))

    async def from_button(self, event):
        await self.send(text_data=json.dumps({"message": "from_button"}))

    async def transaction_updated(self, event):
        print("called transaction_updated")
        await self.send(text_data=json.dumps({"message": "from model update"}))
