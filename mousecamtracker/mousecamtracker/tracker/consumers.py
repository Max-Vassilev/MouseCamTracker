import json
from channels.generic.websocket import WebsocketConsumer
from mousecamtracker.tracker.models import *

class MouseConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    # Called when a message is received from the WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        x = data['x']
        y = data['y']

        # Send a JSON-encoded message back to the WebSocket client
        self.send(text_data=json.dumps({
            'x': x,
            'y': y
        }))
