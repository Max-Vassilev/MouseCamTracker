import json
import cv2
from channels.generic.websocket import WebsocketConsumer
from mousecamtracker.tracker.models import MouseData
import os
from django.conf import settings

class MouseTrackingConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        x = data['x']
        y = data['y']

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

        # Capture image using OpenCV
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            image_number = len([f for f in os.listdir(settings.MEDIA_ROOT)]) + 1
            image_filename = f'mouse_click_{image_number}.png'
            image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

            # Save the image to the image path
            cv2.imwrite(image_path, frame)

            # Save the data to the database
            MouseData.objects.create(x_coordinate=x, y_coordinate=y, image_path=image_filename)
