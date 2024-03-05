import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DashboardConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        
        await self.accept()


    async def disconnect(self, close_code):

        print(f'Connection closed with code: {close_code}')
        

    async def recieve(self, text_data):
        text_data_json = json.loads(text_data)

        # message = text_data_json['message']
        # sender = text_data_json['sender']

        print(text_data_json)

        await self.send(text_data=json.dumps({
            'message': 'Hello world',
            # 'sender':sender
        }))
        print('passing here line 30')

        