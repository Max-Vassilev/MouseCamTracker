from django.shortcuts import render

def index(request):
    return render(request, 'mouse_tracker.html')
