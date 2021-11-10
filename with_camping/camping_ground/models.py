from django.db import models

# Create your models here.
class CampingGround(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)

    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)

    body = models.CharField(max_length = 300)