from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello from Flights');
def Flight_search(request, origin, destination):
    return HttpResponse("Showing Flights from {} to {}".format(origin, destination))
##request, origin,destination