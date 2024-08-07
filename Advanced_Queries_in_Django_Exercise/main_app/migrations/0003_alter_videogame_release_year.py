# Generated by Django 5.0.4 on 2024-08-01 13:26

import main_app.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_videogame_rating_alter_videogame_release_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='release_year',
            field=models.PositiveIntegerField(validators=[main_app.custom_validators.ValueInRangeValidator(1990, 2023, message='The release year must be between 1990 and 2023')]),
        ),
    ]
