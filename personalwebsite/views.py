from django.shortcuts import render

def index(request):
    return render(request, 'personalwebsite/index.html', {})

def photos(request):
    return render(request, 'personalwebsite/photos.html', {})