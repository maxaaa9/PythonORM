# Generated by Django 5.0.4 on 2024-07-11 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='subject',
            new_name='subjects',
        ),
        migrations.AlterField(
            model_name='subject',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.lecturer'),
        ),
    ]
