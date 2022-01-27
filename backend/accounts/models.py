from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True)
    Phone = models.CharField(max_length=13, blank=True)
    address = models.CharField(max_length=100, blank=True)
    pass


