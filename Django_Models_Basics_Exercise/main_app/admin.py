from django.contrib import admin

from main_app.models import Book


# Register your models here.
@admin.register(Book)
class Book(admin.ModelAdmin):
    pass
