from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Member(AbstractUser):
    people_name = models.CharField(max_length= 30)
    nickname = models.CharField(max_length = 30)
