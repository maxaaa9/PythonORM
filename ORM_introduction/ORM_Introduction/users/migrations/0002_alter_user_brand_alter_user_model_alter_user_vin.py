# Generated by Django 5.0.6 on 2024-06-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Brand',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='Model',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='VIN',
            field=models.CharField(max_length=30),
        ),
    ]
