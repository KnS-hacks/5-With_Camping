from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    nickname = models.CharField(max_length = 30)