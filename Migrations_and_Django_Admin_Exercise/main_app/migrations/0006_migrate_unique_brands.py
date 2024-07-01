# Generated by Django 5.0.4 on 2024-06-27 12:54

from django.db import migrations


class Migration(migrations.Migration):
    def create_unique_brands(apps, schema_editor):
        shoe = apps.get_model('main_app', 'Shoe')
        unique_brands = apps.get_model('main_app', 'UniqueBrands')

        unique_brands_names = shoe.objects.values_list('brand', flat=True).distinct()
        unique_brands.objects.bulk_create([unique_brands(brand_name=name) for name in unique_brands_names])

    def reverse_unique_brands(apps, schema_editor):
        unique_brands = apps.get_model('main_app', 'UniqueBrands')
        unique_brands.objects.all().delete()

    dependencies = [
        ('main_app', '0005_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_unique_brands)
    ]
