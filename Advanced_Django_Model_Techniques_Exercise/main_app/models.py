from django.db import models
from django.core.validators import RegexValidator, URLValidator, MinValueValidator, MinLengthValidator
from main_app.custom_validators import validate_name_only_letters_and_space
from decimal import Decimal
from main_app.mixins import RechargeEnergyMixin
from django.contrib.postgres.search import SearchVectorField


# Create your models here.


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validate_name_only_letters_and_space,])

    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18, message="Age must be greater than or equal to 18"),])

    email = models.EmailField(error_messages={'invalid': 'Enter a valid email address'})

    phone_number = models.CharField(
        max_length=13,
        validators=[RegexValidator(regex=r'^\+359[0-9]{9}$',
                                   message="Phone number must start with '+359' followed by 9 digits")])

    website_url = models.URLField(error_messages={'invalid': 'Enter a valid URL'})


class BaseMedia(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Book(BaseMedia):
    author = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(5, "Author must be at least 5 characters long")])

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[MinLengthValidator(6, "ISBN must be at least 6 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'


class Movie(BaseMedia):
    director = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(8, "Director must be at least 8 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'


class Music(BaseMedia):
    artist = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(9, "Artist must be at least 9 characters long")])

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        tax_rate = 8
        return (self.price * tax_rate) / 100

    def calculate_shipping_cost(self, weight: Decimal):
        shipping_cost_multiplier = Decimal(2.00)
        return weight * shipping_cost_multiplier

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        percentage_original_price = Decimal(20)
        return self.price + (self.price * percentage_original_price) / 100

    def calculate_tax(self):
        tax_rate = 5
        return (self.price * tax_rate) / 100

    def calculate_shipping_cost(self, weight: Decimal):
        shipping_cost_multiplier = Decimal(1.50)
        return weight * shipping_cost_multiplier

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


class Hero(models.Model, RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField()


class SpiderHero(Hero):

    class Meta:
        proxy = True

    def swing_from_buildings(self):
        energy_cost = 80
        if self.energy < energy_cost:
            return f"{self.name} as Spider Hero is out of web shooter fluid"

        self.energy -= energy_cost
        if self.energy == 0:
            self.energy = 1

        self.save()
        return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):

    class Meta:
        proxy = True

    def run_at_super_speed(self):
        energy_cost = 65
        if self.energy < energy_cost:
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.energy -= energy_cost
        if self.energy == 0:
            self.energy = 1

        self.save()
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"


class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    search_vector = SearchVectorField(
        null=True
    )

    class Meta:
        indexes = [models.Index(fields=['search_vector'])]
