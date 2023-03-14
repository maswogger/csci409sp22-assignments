from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight
from airports.models import Airport

def index(request):
    # Fetch all flights
    Flights = Flight.objects.all()
    Flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code for f in Flights])
    return HttpResponse('Listing all flights: ' + Flight_list)

def Flight_search(request, origin, destination):
    origin_airport = Airport.objects.get(airport_code=origin)
    destination_airport = Airport.objects.get(airport_code=destination)
    # Get flights with matching origin and destination airports
    Flights = Flight.objects.filter(origin_id=origin_airport, destination_id=destination_airport)
    Flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in Flights])
    return HttpResponse('Showing flights: ' + Flight_list)

