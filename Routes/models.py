from django.db import models
class Airline(models.Model):
    airline_name = models.CharField(max_length=100)
    airline_code = models.CharField(max_length=2)
class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight_number = models.IntegerField()
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
# Create your models here.
