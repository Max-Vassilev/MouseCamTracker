from django.contrib import admin
from .models import MouseData

@admin.register(MouseData)
class MouseDataAdmin(admin.ModelAdmin):
    list_display = ('x_coordinate', 'y_coordinate', 'image_path')
    search_fields = ('x_coordinate', 'y_coordinate')
