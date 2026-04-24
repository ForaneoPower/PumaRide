from django.db import models

class Service(models.Model):
    date_time = models.DateTimeField("date_time")
    flux = models.FloatField(default = 0.0)