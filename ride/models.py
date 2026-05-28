from django.db import models

class RideRequest(models.Model):
    start_name = models.CharField(max_length=255)   #Nombre del punto de inicio
    end_name = models.CharField(max_length=255)     #Nombre del punto de final
    start_lng = models.FloatField()            #Longitud en la que inicia
    start_lat = models.FloatField()            #Latitud donde inicia
    end_lng = models.FloatField()          #Longitud donde termina
    end_lat = models.FloatField()      #Latitud donde termina

    distance_km = models.FloatField(null=True, blank=True)    #Distancia en km
    duration_min = models.FloatField(null=True, blank=True)    #Duration_min

