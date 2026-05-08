from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.index, name='index'),
    path('request/', views.request_ride, name='request_ride'),
    path('confirmation/<int:pk>/', views.confirmation, name='confirmation'),
]