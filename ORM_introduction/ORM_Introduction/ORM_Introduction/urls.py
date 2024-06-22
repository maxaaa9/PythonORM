from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def test_function(request):
    return HttpResponse("Hello World!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
