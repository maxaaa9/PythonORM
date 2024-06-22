from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_function(request):
    return HttpResponse("Hello Users, im coming from views!")
