from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello from Flights');
def Ticket_search(request, confirmation_number):
    return HttpResponse("Search for tickets confirmation number:  {}".format(confirmation_number))