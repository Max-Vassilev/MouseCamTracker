from django.db import models

class MouseData(models.Model):
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    image_path = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Mouse Data Instance" 
        verbose_name_plural = "Mouse Data Instances"  

    def __str__(self):
        return f"MouseData(x={self.x_coordinate}, y={self.y_coordinate})"
