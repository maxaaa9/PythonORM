# Generated by Django 5.0.4 on 2024-07-15 18:55

import django.db.models.deletion
import main_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('sound', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('license_number', models.CharField(max_length=10)),
                ('availability', main_app.models.BooleanChoiceField(choices=[(True, 'Available'), (False, 'Not Available')], default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Veterinarians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('license_number', models.CharField(max_length=10)),
                ('availability', main_app.models.BooleanChoiceField(choices=[(True, 'Available'), (False, 'Not Available')], default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.animal')),
                ('wing_span', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            bases=('main_app.animal',),
        ),
        migrations.CreateModel(
            name='Mammal',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.animal')),
                ('fur_color', models.CharField(max_length=50)),
            ],
            bases=('main_app.animal',),
        ),
        migrations.CreateModel(
            name='Reptile',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.animal')),
                ('scale_type', models.CharField(max_length=50)),
            ],
            bases=('main_app.animal',),
        ),
        migrations.CreateModel(
            name='ZooDisplayAnimal',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main_app.animal',),
        ),
        migrations.CreateModel(
            name='ZooKeeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('specialty', models.CharField(choices=[('Mammals', 'Mammals'), ('Birds', 'Birds'), ('Reptile', 'Reptile'), ('Others', 'Others')], max_length=10)),
                ('managed_animals', models.ManyToManyField(to='main_app.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
