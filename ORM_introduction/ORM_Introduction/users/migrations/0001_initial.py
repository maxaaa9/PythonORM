# Generated by Django 5.0.6 on 2024-06-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VIN', models.CharField(max_length=18)),
                ('Brand', models.CharField(max_length=20)),
                ('Model', models.CharField(max_length=20)),
                ('IS_CAR', models.BooleanField(default=False)),
            ],
        ),
    ]
