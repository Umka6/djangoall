from django.shortcuts import render
from .models import Portfolio


def index(request):
    port = Portfolio.objects.all()
    return render(request, 'myapp/index.html', {'portfolio': port})
