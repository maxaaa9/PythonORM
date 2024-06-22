from django.http import HttpResponse
from django.urls import path
from . import views




urlpatterns = [
    path('test/', views.test_function),
]
