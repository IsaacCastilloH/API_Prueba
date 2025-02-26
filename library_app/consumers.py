from channels.generic.websocket import AsyncWebsocketConsumer
import json

class BibliotecaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "biblioteca_updates",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "biblioteca_updates",
            self.channel_name
        )

    async def libro_reservado(self, event):
        await self.send(text_data=json.dumps(event))