from django.shortcuts import render, redirect
from .models import RideRequest
from .forms import RideRequestForm
import httpx

FastAPI_URL = "http://localhost:8001" 

def index(request):
    return render(request, 'ride/index.html')

def request_ride(request):
    if request.method == 'POST':
        form = RideRequestForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)

            start = f"{ride.start_lng},{ride.start_lat}"
            end = f"{ride.end_lng},{ride.end_lat}"
            response = httpx.get(f"{FastAPI_URL}/route", params={"start": start, "end": end})
            data = response.json()
            ride.distance_km = data.get("distance_km")
            ride.duration_min = data.get("duration_min")

            ride.save()
            return redirect('confirmation', pk=ride.pk)
    else:
        form = RideRequestForm()
    return render(request, 'ride/index.html', {'form': form})

def confirmation(request, pk):
    ride = RideRequest.objects.get(pk=pk)
    return render(request, 'ride/confirmation.html', {'ride': ride})

def passenger_profile(request):
    return render(request, 'ride/passenger_profile.html')

def driver_profile(request):  
    return render(request, 'ride/driver_profile.html')