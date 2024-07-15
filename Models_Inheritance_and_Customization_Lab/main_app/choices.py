from main_app import models
from django.db import models


class ZooKeeperChoices(models.TextChoices):
    Mammals = 'Mammals'
    Birds = 'Birds'
    Reptile = 'Reptile'
    Others = 'Others'

