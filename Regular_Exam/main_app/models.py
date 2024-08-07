from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from main_app.custom_choices import StatusChoices
from main_app.custom_managers import AstronautManager


# Create your models here.
class Astronaut(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)])

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(r'^\d+$')]
    )

    is_active = models.BooleanField(
        default=True
    )

    date_of_birth = models.DateField(null=True, blank=True)

    spacewalks = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    manufacturer = models.CharField(
        max_length=100
    )

    capacity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )

    weight = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    launch_date = models.DateField()

    updated_at = models.DateTimeField(
        auto_now=True,
    )


class Mission(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)]
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=9,
        choices=StatusChoices,
        default='Planned'
    )

    launch_date = models.DateField()

    updated_at = models.DateTimeField(auto_now=True)

    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE)

    astronauts = models.ManyToManyField(
        to=Astronaut,
        related_name='missions'
    )

    commander = models.ForeignKey(
        to=Astronaut,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
