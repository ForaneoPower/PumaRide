from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.index, name='index'),
    path('request/', views.request_ride, name='request_ride'),
    path('confirmation/<int:pk>/', views.confirmation, name='confirmation'),
    path('passenger_profile/', views.passenger_profile, name= 'passenger_profile'),
    path('driver_profile/', views.driver_profile, name ='driver_profile')
]