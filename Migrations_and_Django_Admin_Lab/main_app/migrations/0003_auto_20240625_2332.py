# Generated by Django 5.0.6 on 2024-06-25 20:32
import random

from django.db import migrations


class Migration(migrations.Migration):
    def generate_barcodes(apps, schema_editor):
        Product = apps.get_model('main_app', 'Product')
        all_products = Product.objects.all()
        barcode = random.sample(range(100_000_000, 999_999_999 + 1), len(all_products))
        for product, barcode in zip(all_products, barcode):
            product.barcode = barcode
            product.save()

    def reverse_barcodes(apps, schema_editor):
        Product = apps.get_model('main_app', 'Product')
        for product in Product.objects.all():
            product.barcode = 0
            product.save()
    dependencies = [
        ('main_app', '0002_product_created_on_product_last_edited_on'),
    ]

    operations = [
        migrations.RunPython(generate_barcodes, reverse_barcodes)
    ]
