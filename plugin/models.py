from django.db import models

class Routing(models.Model):
    start_name = models.CharField(max_length=100)
    destination_name = models.CharField(max_length=100)
    duration = models.FloatField()
    distance = models.FloatField()
