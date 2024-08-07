from django.db import models
from django.db.models import Count


class AstronautManager(models.Manager):

    def get_astronauts_by_missions_count(self):
        return self.get_queryset().annotate(total_missions=Count('missions')).order_by('-total_missions', 'phone_number')
