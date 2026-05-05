from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('request/', views.request_ride, name='request_ride'),
    path('ride/<int:ride_id>/', views.ride_detail, name='ride_detail'),
]