import json
from channels.generic.websocket import WebsocketConsumer

class MouseConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):      

        data = json.loads(text_data)
        # Example of text_data: {"x": 1620,"y": 343}

        x = data['x']
        y = data['y']
        self.send(text_data=json.dumps({
            'x': x,
            'y': y
        }))
