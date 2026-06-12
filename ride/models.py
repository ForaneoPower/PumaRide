from django.db import models
from django.contrib.auth.models import AbstractUser

class RideRequest(models.Model):
    start_name = models.CharField(max_length=255)
    end_name = models.CharField(max_length=255)
    start_lng = models.FloatField()
    start_lat = models.FloatField()
    end_lng = models.FloatField()
    end_lat = models.FloatField()

    distance_km = models.FloatField(null=True, blank=True)
    duration_min = models.FloatField(null=True, blank=True)

class User(AbstractUser):
    student_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    institution = models.CharField(max_length=100, default='UNAM Morelia')
    campus = models.CharField(max_length=100, default='Morelia, Mich.')
    rides_taken = models.IntegerField(default=0)
    score = models.FloatField(default=5.0)

    def __str__(self):
        return self.get_full_name()


class Driver(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, related_name='driver_profile')
    license_number = models.CharField(max_length=20, unique=True)
    driver_since = models.CharField(max_length=30)
    vehicle_plate = models.CharField(max_length=15, unique=True)
    vehicle_capacity = models.IntegerField(default=4)
    rides_given = models.IntegerField(default=0)
    score = models.FloatField(default=5.0)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.vehicle_plate}"