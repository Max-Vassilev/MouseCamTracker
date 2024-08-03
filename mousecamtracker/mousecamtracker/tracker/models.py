from django.db import models

class MouseData(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return f"Mouse at ({self.x_coordinate}, {self.y_coordinate})"
