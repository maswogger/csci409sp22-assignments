
from django.urls import path
from . import views

urlpatterns = [
    path('/<int:confirmation_number>/', views.Ticket_search, name='Ticket_search'),
]