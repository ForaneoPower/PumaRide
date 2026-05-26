from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title': 'Welcome to PumaRide App',
    }
    
    return render(request, 'core/home.html', context)