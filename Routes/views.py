from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello from Routes');
def Routes_search(request, origin, destination):
    return HttpResponse("Showing Routes from {} to {}".format(origin, destination))