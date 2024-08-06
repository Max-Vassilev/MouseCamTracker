import json
from channels.generic.websocket import WebsocketConsumer
from mousecamtracker.tracker.models import *

class MouseTrackingConsumer(WebsocketConsumer):
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


class MouseClickConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        x = data['x']
        y = data['y']

        # Save the coordinates and a placeholder image path to the database
        MouseData.objects.create(x_coordinate=x, y_coordinate=y, image_path="test")
