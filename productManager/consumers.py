import json
from channels.generic.websocket import AsyncWebsocketConsumer


class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Entra no grupo "global_stock"
        await self.channel_layer.group_add("global_stock", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Sai do grupo
        await self.channel_layer.group_discard("global_stock", self.channel_name)

    # Método chamado quando o grupo recebe uma mensagem
    async def stock_update(self, event):
        message = event["message"]

        # Envia para o WebSocket do cliente
        await self.send(text_data=json.dumps({"type": "stock_update", "data": message}))
