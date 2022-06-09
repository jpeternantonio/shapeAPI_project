from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Shape(models.Model):
    name = models.CharField(max_length=100)
    side = models.IntegerField()
    height = models.IntegerField()
    base = models.IntegerField()


    def __str__(self):
        return self.name