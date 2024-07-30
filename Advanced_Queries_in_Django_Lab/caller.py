import os
from decimal import Decimal
from pprint import pprint

import django
from django.db import connections, connection
from django.db.models import Sum, Q, F
from unicodedata import decimal

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product, Category, Customer, Order, OrderProduct


# Create and run queries
def product_quantity_ordered():
    products = []

    for p in Product.objects.annotate(
            quantity=Sum('orderproduct__quantity')).exclude(quantity=None).order_by('-quantity'):
        products.append(f"Quantity ordered of {p.name}: {p.quantity}")

    return '\n'.join(products)


def ordered_products_per_customer():
    order_info = []
    # objects = Order.objects.prefetch_related('products').all()
    # for order in objects:
    #     order_info.append(f'Order ID: {order.id}, Customer: {order.customer.username}')
    #     for product_category in order.products.all():
    #         order_info.append(f'- Product: {product_category.name}, Category: {product_category.category.name}')
    #         # 13 queries

    # objects = Order.objects.prefetch_related('orderproduct_set__product__category')
    # for order in objects:
    #     order_info.append(f'Order ID: {order.id}, Customer: {order.customer.username}')
    #     for product_category in order.orderproduct_set.all():
    #         order_info.append(f'- Product: {product_category.product.name}, Category: {product_category.product.category.name}')
    #         # 7 queries

    # objects = Order.objects.prefetch_related('products').all()
    # for order in objects:
    #     order_info.append(f'Order ID: {order.id}, Customer: {order.customer.username}')
    #     for product_category in order.orderproduct_set.all():
    #         order_info.append(f'- Product: {product_category.product.name}, Category: {product_category.product.category.name}')
    #         # 24 queries

    objects = (
        Order.objects
        .select_related('customer')  # Efficiently join Order and Customer tables
        .prefetch_related('orderproduct_set__product__category')  # Prefetch related products and categories
        .all()
    )

    for order in objects:
        order_info.append(f'Order ID: {order.id}, Customer: {order.customer.username}')
        for order_product in order.orderproduct_set.all():
            product = order_product.product
            category = product.category
            order_info.append(f'- Product: {product.name}, Category: {category.name}')

            # 4 queries - most optimal way

    return '\n'.join(order_info)


def filter_products():
    products = []
    query = Q(is_available=True) & Q(price__gt=3.00)
    for product in Product.objects.filter(query).order_by('-price', 'name'):
        products.append(f"{product.name}: {product.price}lv.")

    return '\n'.join(products)


def give_discount():
    products = []
    query = Q(is_available=True) & Q(price__gt=3.00)
    Product.objects.filter(query).update(price=F('price') * 0.7)

    for product in Product.objects.filter(is_available=True).order_by('-price', 'name'):
        products.append(f"{product.name}: {product.price}lv.")

    return '\n'.join(products)


print(give_discount())
pprint(connection.queries)
