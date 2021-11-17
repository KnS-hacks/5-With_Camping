from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    image = models.ImageField(upload_to = "account/", blank=True, null=True)
    nickname = models.CharField(max_length = 30)
