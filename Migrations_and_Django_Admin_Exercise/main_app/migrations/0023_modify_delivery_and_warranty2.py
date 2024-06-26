# Generated by Django 5.0.6 on 2024-07-01 13:47
from django.utils import timezone

from django.db import migrations


def modify_delivery_and_warranty_by_status(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')
    orders_objects = order_model.objects.all()

    for order in orders_objects:
        if order.status == 'Pending':
            order.delivery = order.order_date + timezone.timedelta(days=3)
        elif order.status == 'Completed':
            order.warranty = '24 months'
        elif order.status == 'Cancelled':
            order.delete()
            continue

        order.save()


def reverse_modify_delivery_and_warranty_by_default(apps, schema_editor):
    order_model = apps.get_model('main_app', 'Order')

    for order in order_model.objects.all():
        if order.status != 'Pending':
            order.warranty = order._meta.get_field('warranty').default
        order.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_alter_order_delivery'),
    ]

    operations = [
        migrations.RunPython(modify_delivery_and_warranty_by_status, reverse_modify_delivery_and_warranty_by_default)
    ]
