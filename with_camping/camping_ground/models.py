from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class CampingGround(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)

    latitude = models.FloatField(default = 0.0)
    longitude = models.FloatField(default = 0.0)

    body = models.CharField(max_length = 300)
    desc_img = models.ImageField(upload_to='desc_img', blank=True, null=True)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default = 1)
    price = models.IntegerField(default=10000)
