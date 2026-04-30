from django.db import models

class RideRequest(models.Model):
    # values
    start_name = models.CharField(max_length=255)
    end_name = models.CharField(max_length=255)
    start_lng = models.FloatField()
    start_lat = models.FloatField()
    end_lng = models.FloatField()
    end_lat = models.FloatField()

    distance_km = models.FloatField(null=True, blank=True)
    duration_min = models.FloatField(null=True, blank=True)

