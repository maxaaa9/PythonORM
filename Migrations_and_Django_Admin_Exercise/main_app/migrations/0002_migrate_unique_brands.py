# Generated by Django 5.0.4 on 2024-06-26 22:03

from django.db import migrations

from main_app import models


class Migration(migrations.Migration):
    def UniqueBrands(apps, schema_editor):
        brand_name = models.CharField(max_length=25, unique=True)

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
    ]
