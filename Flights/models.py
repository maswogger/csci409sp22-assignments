from django.db import models
from airports.models import Airport

class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    airline_code = models.CharField(max_length=2)
    from django.db import models
    from airports.models import Airport

class Flight(models.Model):
        airline = models.ForeignKey(Airline, on_delete=models.CASCADE, default=1)
        flight_number = models.IntegerField()
        origin = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='flight_origin')
        destination = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='flight_destination')
        departure = models.DateTimeField()
        arrival = models.DateTimeField()
        aircraft_type = models.CharField(max_length=10)



