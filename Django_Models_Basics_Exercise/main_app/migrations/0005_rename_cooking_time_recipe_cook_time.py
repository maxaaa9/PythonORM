# Generated by Django 5.0.4 on 2024-06-23 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_exercise_product_recipe_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cooking_time',
            new_name='cook_time',
        ),
    ]