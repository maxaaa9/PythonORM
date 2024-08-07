# Generated by Django 5.0.4 on 2024-07-22 17:42

import django.core.validators
import main_app.custom_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[main_app.custom_validators.validate_name_only_letters_and_space])),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18, message='Age must be greater than or equal to 18')])),
                ('email', models.EmailField(error_messages={'invalid': 'Enter a valid email address'}, max_length=254)),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must start with '+359' followed by 9 digits", regex='^\\+359[0-9]{9}$')])),
                ('website_url', models.URLField(error_messages={'invalid': 'Enter a valid URL'})),
            ],
        ),
    ]
