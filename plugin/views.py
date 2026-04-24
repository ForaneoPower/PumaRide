from django.shortcuts import render
from django.http import HttpResponse
from .models import Service


def index(request):
    return HttpResponse("Hello, this is the plugin index page.")