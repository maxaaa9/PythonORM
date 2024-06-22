from django.db import models

# Create your models here.
class User(models.Model):
    VIN = models.CharField(max_length=30)
    Brand = models.CharField(max_length=30)
    Model = models.CharField(max_length=30)
    IS_CAR = models.BooleanField(default=False)
