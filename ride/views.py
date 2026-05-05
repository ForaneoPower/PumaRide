from django.shortcuts import render, redirect
from .models import RideRequest
from .forms import RideRequestForm
import httpx

FastAPI_URL = "http://localhost:8000" 

def index(request):
    return render(request, 'ride/index.html')

def request_ride(request):
    if request.method == 'POST':
        form = RideRequestForm(request.POST)
        if form.is_valid():
            route_data = httpx.get(f"{FastAPI_URL}/route", params={
                "start": f"{form.cleaned_data['start_lng']},{form.cleaned_data['start_lat']}",
                "end": f"{form.cleaned_data['end_lng']},{form.cleaned_data['end_lat']}"
            }).json()

            ride = form.save(commit=False)
            ride.start_name = form.cleaned_data['start_name']
            ride.end_name = form.cleaned_data['end_name']
            ride.distance_km = route_data['distance_km']
            ride.duration_min = route_data['duration_min']
            ride.save()
            return redirect('ride_detail', ride_id=ride.id)
            
    else:
        form = RideRequestForm()
    
    return render(request, 'ride/request_ride.html', {'form': form})

def ride_detail(request, ride_id):
    ride = RideRequest.objects.get(id=ride_id)
    return render(request, 'ride/ride_detail.html', {'ride': ride})