from django.shortcuts import render
from django.http import HttpResponse
from .models import Routing


def index(request):
    routes = Routing.objects.all()
    return render(request, 'plugin/index.html', {'routes': routes})