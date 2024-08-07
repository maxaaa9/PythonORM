from django.db import models


class StatusChoices(models.TextChoices):
    PLANNED = 'Planned'
    ONGOING = 'Ongoing'
    COMPLETED = 'Completed'
