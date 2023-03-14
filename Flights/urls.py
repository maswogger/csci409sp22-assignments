from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('/search/<str:origin>/<str:destination>/', views.Flight_search, name='Flight_search'),
]
